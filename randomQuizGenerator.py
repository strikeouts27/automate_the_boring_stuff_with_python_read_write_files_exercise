#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random


# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.


# Create the quiz and answer key files
for quizNum in range(35):
    with (
        open(f"capitalsquiz{quizNum + 1}.txt", "a") as quizFile,
        open(f"capitalsquiz_answers{quizNum + 1}.txt", "a") as answerKeyFile,
    ):
        pass

        # TODO: Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)

# TODO: Loop through all 50 states, making a question for each.

        for questionNum in range(50): 
            correct_Answer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correct_Answer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correct_Answer]
            random.shuffle(answerOptions)

    # Loop through all 50 states, making a question for each.

    # Write the question and the answer options to the quiz file.

        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        
        for i in range(4): 
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')

        # Write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correct_Answer)]}")
