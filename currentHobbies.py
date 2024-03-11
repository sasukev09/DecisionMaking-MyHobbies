from random import choice

# List of hobbies
hobbies_2024 = [['workout', 'forever', '4-7 times', 'any mood'],
                ['duolingo', 'forever', '7 times', 'any mood'],
                ['protein', 'forever', '5 times', 'any mood'],
                ['music', 'often', '4 times', 'focus'],
                ['fun music', 'often', '4 times', 'fun'],
                ['sad music', 'rare', '2 times', 'sad']]

# input current mood
print('How do you feel today, what is your mood?')
myMood = input()

# Loop through the list and find that specific mood
for item in hobbies_2024:
    if item[3] == myMood:
        print('You should do ' + item[0] + ' if you feel ' + myMood + '.')


