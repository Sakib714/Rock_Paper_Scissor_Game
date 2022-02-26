from random import choice
import pyttsx3
from time import sleep

engine = pyttsx3.init()

# rate
engine.setProperty('rate', 200)

# voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text=text)
    engine.runAndWait()


# welcome msg

welcome_word = 'Welcome to rock papper scissor game. Enter r for rock, enter p for paper and enter s for scissor'

print(welcome_word)
speak(welcome_word)

sleep(1)

speak('How many times do u want to play')
times = int(input('How many times do u want to play: ').lower())


def is_win(user, computer):
    # r>s, p>r, s>p

    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return True


# game start


def play():
    speak('Enter a guess: ')
    user = input('Enter a guess: ')

    computer = choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'You_Won!'

    return 'You Lose'


# Gameplay

point = 0

for i in range(times):

    gg = play()

    print(gg)

    if gg == 'You_Won!':
        point += 1

print(f'Total Point: ', point)

# Calculate percentage

percent = (point/times)*100

print(f'You Scored total {percent}%')

# Speak result

speak(f'Your total point is {point}')
speak(f'You scored total {percent}percent')

if percent < float(35):
    speak("You scored less then 35 percent! I think i am smarter then u!")

elif float(35) < percent < float(60):
    speak("You scored an average total. But I think i can beat you in guessing. if you play like this soon AI will take over the world. ha ha ha ha")

elif float(60)< percent <float(85):
    speak('Well done. But not the best score. Ghost! soo close to 100 percent!')

elif float(85)<percent<float(100):
    speak('Congrats! You have a good brain. When AI will take over the world. i will refer my friend not to kill you. We can use your brain for our development!')

else:
    speak('Something went wrong!')