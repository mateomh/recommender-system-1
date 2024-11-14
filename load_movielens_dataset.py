def load_movielens():
  movies = {}
  for row in open('/content/u.item', encoding = 'ISO-8859-1'):
    (id, name) = row.split('|')[0:2]
    movies[id] = name

  dataset = {}
  for row in open('/content/u.data'):
    (user, movie_id, score, time) = row.split('\t')
    dataset.setdefault(user, {})
    dataset[user][movies[movie_id]] = float(score)
  return dataset