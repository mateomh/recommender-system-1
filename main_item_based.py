from item_based_filtering.get_item_recommendation import get_item_recommendation
from datasets.movies_by_user_rating import movies_by_user as users_feedback_movies
from item_based_filtering.calculate_item_similarities import calculate_item_similarities
from datasets.users_dataset import users_feedback
from print_user_recommendation import print_user_recommendation


similarities = calculate_item_similarities(users_feedback_movies)

# Recommendations for a single user
print(get_item_recommendation(users_feedback, similarities, 'Fred'))

# Top Recommendation for all the users above score of 3
print_user_recommendation(get_item_recommendation(users_feedback, similarities, 'Fred'), 3)
print_user_recommendation(get_item_recommendation(users_feedback, similarities, 'Stuart'), 3)
print_user_recommendation(get_item_recommendation(users_feedback, similarities, 'Jessica'), 3)
print_user_recommendation(get_item_recommendation(users_feedback, similarities, 'Suzane'), 3)

