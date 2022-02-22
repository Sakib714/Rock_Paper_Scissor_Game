from random import choice
import pyttsx3





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


speak('How many times do u want to play')
times = int(input('How many times do u want to play: '))



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


        return 'You Won!'

    return 'You Lose'


# Gameplay

for i in range(times):
    print(play())

