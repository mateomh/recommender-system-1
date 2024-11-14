from euclidian_distance import euclidian_distance

def get_user_recommendation(dataset, user):
  totals = {}
  sum_similarity = {}
  for other in dataset:
    if other == user:
      continue    
    
    similarity = euclidian_distance(dataset, user, other)

    if similarity == 0:
      continue

    for item in dataset[other]:
      if item not in dataset[user]:
        totals.setdefault(item, 0)
        totals[item] += dataset[other][item] * similarity

        sum_similarity.setdefault(item, 0)
        sum_similarity[item] += similarity

  recommendations = [(total / sum_similarity[item], item) for item, total in totals.items()]  
  recommendations.sort()
  recommendations.reverse()
  return recommendations