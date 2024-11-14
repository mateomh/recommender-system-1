def get_item_recommendation(user_dataset, similarities, user):
  scores = {}
  totals = {}
  user_scores = user_dataset[user]
  for (item, score) in user_scores.items():
    for (similarity, item2) in similarities[item]:
      if item2 in user_scores:
        continue
      scores.setdefault(item2, 0)
      scores[item2] += similarity * score
      totals.setdefault(item2, 0)
      totals[item2] += similarity
  
  recommendations = [(score / totals[item], item) for item, score in scores.items()]
  recommendations.sort()
  recommendations.reverse()
  return recommendations
