import datetime
from datetime import timedelta
from collections import defaultdict

import requests as req
from bs4 import BeautifulSoup
import json

today = datetime.date.today()

data = {
    'action': 'loadmore',
    'query': '''
    'a:63:{s:13:"category_name";s:4:"news";s:5:"error";s:0:"";
    s:1:"m";s:0:"";s:1:"p";i:0;s:11:"post_parent";s:0:"";s:7:"subpost";s:0:"";s:10:"subpost_id";
    s:0:"";s:10:"attachment";s:0:"";s:13:"attachment_id";i:0;s:4:"name";s:0:"";s:8:"pagename";
    s:0:"";s:7:"page_id";i:0;s:6:"second";s:0:"";s:6:"minute";s:0:"";s:4:"hour";s:0:"";s:3:"day";
    i:0;s:8:"monthnum";i:0;s:4:"year";i:0;s:1:"w";i:0;s:3:"tag";s:0:"";s:3:"cat";i:141;s:6:"tag_id";s:0:"";
    s:6:"author";s:0:"";s:11:"author_name";s:0:"";s:4:"feed";s:0:"";s:2:"tb";s:0:"";s:5:"paged";i:0;s:8:"meta_key";
    s:0:"";s:10:"meta_value";s:0:"";s:7:"preview";s:0:"";s:1:"s";s:0:"";s:8:"sentence";s:0:"";s:5:"title";s:0:"";
    s:6:"fields";s:0:"";s:10:"menu_order";s:0:"";s:5:"embed";s:0:"";s:12:"category__in";a:0:{}s:16:"category__not_in";
    a:0:{}s:13:"category__and";a:0:{}s:8:"post__in";a:0:{}s:12:"post__not_in";a:0:{}s:13:"post_name__in";
    a:0:{}s:7:"tag__in";a:0:{}s:11:"tag__not_in";a:0:{}s:8:"tag__and";a:0:{}s:12:"tag_slug__in";
    a:0:{}s:13:"tag_slug__and";a:0:{}s:15:"post_parent__in";a:0:{}s:19:"post_parent__not_in";
    a:0:{}s:10:"author__in";a:0:{}s:14:"author__not_in";a:0:{}s:14:"posts_per_page";i:12;s:19:"ignore_sticky_posts";
    b:0;s:16:"suppress_filters";b:0;s:13:"cache_results";b:0;s:22:"update_post_term_cache";b:1;
    s:19:"lazy_load_term_meta";b:1;s:22:"update_post_meta_cache";b:1;s:9:"post_type";s:0:"";s:8:"nopaging";b:0;
    s:17:"comments_per_page";s:2:"50";s:13:"no_found_rows";b:0;s:5:"order";s:4:"DESC";}'
    ''',
    'post_id': '',
    'page': 1,
    'last_date': today.strftime('%d.%m.%Y')
}

nonBreakSpace = u'\xa0'


def building_corpus():
    date = today.strftime('%d.%m.%Y')
    news_data = defaultdict(list)

    def _make_record(tag):
        pattern = {'time': tag.time.text, 'title': tag.a.text, 'link': tag.a['href']}

        if tag.find('span'):
            pattern['badge'] = tag.a.span.text

        link_response = req.get(pattern['link'])
        soup_link = BeautifulSoup(
            link_response.content.decode('utf-8'), features='html.parser'
        )

        text = ''
        for t in soup_link.find_all('div', {'class': 'single__post'}):
            for p in t.select('p:not(.wp-caption-text)'):
                if p.parent.name == 'blockquote':
                    continue
                text += p.text

        pattern['text'] = text

        return pattern

    response_main = req.get('https://openmedia.io/category/news/')
    soup_main = BeautifulSoup(response_main.content.decode('utf-8'), features='html.parser')
    for tag in soup_main.select('div.news__item, p.news__date'):
        if tag.name == 'p':
            date = tag.text
        else:
            news_data[date].append(_make_record(tag))

    year_ago = today - timedelta(days=366)  # 2020 год високосный
    while True:
        response = req.post('https://openmedia.io/wp-admin/admin-ajax.php', data=data)
        soup = BeautifulSoup(response.text, features='html.parser')
        for tag in soup.select('figure.article'):
            date = tag.select_one('time.article__data').text
            if datetime.datetime.strptime(date, '%d.%m.%Y').date() < year_ago:
                break

            href = tag.select_one('a.article__more').attrs['href']
            link_2_response = req.get(href)
            soup_2_link = BeautifulSoup(
                link_2_response.content.decode('utf-8'), features='html.parser'
            )

            article_text = ''
            try:
                for p in soup_2_link.find('div', {'data-post_id': True}).find_all('p', {'class': False}):
                    article_text += p.text
            except:
                continue

            news_data[date].append({
                'title': tag.select_one('figcaption.article__dscr').text,
                'link': href,
                'text': article_text
            })

        else:
            data['page'] += 1
            continue
        break

    for articles in news_data.values():
        for article in articles:
            article['text'] = article['text'].replace(nonBreakSpace, ' ')

    with open('openmedia_corpus.json', 'w', encoding='utf-8') as file:
        json.dump(news_data, file, indent=2, ensure_ascii=False)

    print('The corpus is compiled!')


if __name__ == '__main__':
    building_corpus()
