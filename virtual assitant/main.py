import speech_recognition as r
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = r.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello!! I am here for you. ')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with r.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sanket' in command:
                command = command.replace('sanket', '')
                print(command)
    except:
        pass
    return command


def run_sanket():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'your name' in command:
        talk('I am sanket')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who  is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Could you please give me  the command .')


while True:
    run_sanket()