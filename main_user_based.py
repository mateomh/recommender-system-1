from datasets.users_dataset import users_feedback
from print_user_recommendation import print_user_recommendation
from user_based_filtering.get_user_recommendation import get_user_recommendation

print('RECOMMENDATIONS FOR FRED')
recommendation = get_user_recommendation(users_feedback, 'Fred')
print_user_recommendation(recommendation, 2)

print('RECOMMENDATIONS FOR STUART')
recommendation = get_user_recommendation(users_feedback, 'Stuart')
print_user_recommendation(recommendation, 2)

print('RECOMMENDATIONS FOR SUZANE')
recommendation = get_user_recommendation(users_feedback, 'Suzane')
print_user_recommendation(recommendation, 2)

print('RECOMMENDATIONS FOR JESSICA')
recommendation = get_user_recommendation(users_feedback, 'Jessica')
print_user_recommendation(recommendation, 2)