import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit


#text-speak engine
engine = pyttsx3.init()

#converting text-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Listening for user input, return the speech 
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source_data:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source_data)
        print("Listening...")
        recognizer.pause_threshold = 1
        audio_data = recognizer.listen(source_data)
        print("Heard something!")
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio_data, language='en-in')
        print(f"User said: {command}\n")
        if "alexa" in command:
                command = command.replace('alexa', '').strip()
        return command.lower()
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("Sorry, I did not catch that. Please repeat.")
    except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there was an issue with the speech recognition service.")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred. Please try again.")
    return "none"

#voice assistant function
def alexa():
    while True:
        command = listen()
        if command == "none":
            continue
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            article = command.replace('wikipedia', '').strip()
            answer = wikipedia.summary(article, sentences=4)
            speak("According to Wikipedia")
            speak(answer)

        elif 'play' in command:
            song = command.replace('play', '').strip()
            speak('Playing ' + song)
            pywhatkit.playonyt(song)


        elif 'time' in command:
            time = pywhatkit.time_now()
            speak(f"The time is {time}")

        elif 'date' in command:
            date = pywhatkit.date_today()
            speak(f"Today's date is {date}")

        elif "how are you" in command:
            speak("I am fine, what about you?")

        elif "what is your name" in command:
            speak("I am Alexa, What can I do for you?")

        elif 'stop' in command:
            speak("Goodbye!")
            break

        else:
            print("Sorry, I didn't understand that. Please try again")


if __name__ == "__main__":
    speak("how can i help you?")
    alexa()
