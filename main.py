import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
# engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello, good Morning! How are you?")
    elif hour >= 12 and hour < 18:
        speak("Hello, good Afternoon! How are you?")
    else:
        speak("Hello, good Evening! How are you?")
    speak("I am Victer")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()

    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'notepad' in query:
            note = 'C:\\Windows\\notepad.exe'
            notes = os.listdir(note)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'who made you' in query:
            speak("Bhavyang Bhatt made me alive")
        elif 'who created you' in query:
            speak("Bhavyang Bhatt created me")
        elif 'who developed you' in query:
            speak("Bhavyang Bhatt developed me")
        elif 'who are you' in query:
            speak("I am victor, an A I which is developed by BHAVYANG BHATT through python")
        elif 'describe your self' in query:
            speak("I am victor, an A I which is developed by bhavyang bhatt through python")
        elif 'who is yug' in query:
            speak("Yug is Bhavyang's best friend. In general he is a nice guy. He is the owner of two youtube channels.")
        elif 'ok stop' in query:
            break



