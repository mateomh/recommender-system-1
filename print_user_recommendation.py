def print_user_recommendation(recommendations, min_score):
  for movie in recommendations:
    if movie[0] >= min_score:
      print(movie[1])
