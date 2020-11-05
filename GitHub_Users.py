import sys
import requests as req
from collections import Counter


class GitHubUser:
    def __init__(self, name):
        self.username = name

    def __repr__(self):
        return self.username

    def get_repositories(self):
        r1 = req.get(f'https://api.github.com/users/{self.username}')
        r2 = req.get(r1.json()['repos_url'])
        repositories = r2.json()
        return repositories

    def languages_in_repositories(self):
        c = Counter()
        for repos in self.get_repositories():
            c[repos['language']] += 1
        return c

    def get_followers(self):
        r = req.get(f'https://api.github.com/users/{self.username}/followers')
        followers = r.json()
        return followers


if __name__ == '__main__':
    users = [GitHubUser(name) for name in sys.argv[1:]]
    # Выбирает пользователя из списка и выводит названия его репозиториев, а также их описания.
    selected_idx = int(input(
        f'Доступные пользователи - {[(i, v) for i, v in enumerate(users, start=1)]}.\nКакого пользователя взять? '
    ))
    selected_user = users[selected_idx - 1]
    for dictionary in selected_user.get_repositories():
        print(f'name: {dictionary["name"]}; description: {dictionary["description"]}')

    # Выводит обладателя самого большого количества репозиториев.
    print(max(users, key=lambda user: len(user.get_repositories())))

    # Печатает список языков выбранного пользователя и количество репозиториев, в котором они используются.
    print(selected_user.languages_in_repositories())

    # Выводит язык, наиболее популярный среди пользователей.
    count_languages = Counter()
    for user in users:
        count_languages += user.languages_in_repositories()

    print(count_languages.most_common(1))

    # Выводит пользователя с наибольшим количеством followers.
    print(max(users, key=lambda user: len(user.get_followers())))
