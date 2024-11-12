from euclidian_distance import euclidian_distance

def get_similarities(dataset, user):
  similarity = [(euclidian_distance(dataset, user, other), other) for other in dataset if other != user]
  similarity.sort()
  similarity.reverse()
  return similarity
