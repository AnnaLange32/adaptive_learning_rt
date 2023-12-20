import numpy as np


'''This script saves data into a csv.file'''

emotion_names = ['Enjoyment', 'Boredom', 'Frustration']
emotion_scores = [1, 2, 3]



# Save emotion_names and emotion_scores to 'scores.csv'
np.savetxt('scores.csv', np.column_stack((emotion_names, emotion_scores)), delimiter=',', fmt='%s')

# Zip the lists and save them to 'emotionscores.csv'
#combined_data = list(zip(emotion_names, emotion_scores))
#np.savetxt('emotionscores.csv', combined_data, delimiter=',', fmt='%s')