from gensim.models import Word2Vec
from scipy.spatial.distance import pdist
from sklearn.manifold import TSNE

with open('words_eng.txt', 'r') as file:
    vocab = [[word.rstrip()] for word in file]

    model = Word2Vec(vocab, min_count=1)
    euclidean = pdist(model.wv.vectors)  # евклидово расстояние

    metric_1 = [value for value in euclidean if value <= 0.035]
    metric_2 = [value for value in euclidean if 0.035 < value <= 0.043]
    metric_3 = [value for value in euclidean if value > 0.043]

    tsne = TSNE(n_components=2)
    tsne_model = tsne.fit_transform(model.wv.vectors)

    x = 1
