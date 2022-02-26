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
