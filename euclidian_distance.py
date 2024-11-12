import math

def euclidian_distance(dataset,user1,user2):
  similarity = {}
  for item in dataset[user1]:
    if item in dataset[user2]:
      similarity[item] = 1

  if len(similarity) == 0:
    return 0

  sum_euclidian = sum([math.pow(dataset[user1][item] - dataset[user2][item], 2) for item in dataset[user1] if item in dataset[user2]])

  return 1 / (1 + math.sqrt(sum_euclidian))
