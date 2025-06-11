import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("🔊 Speaking...")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Please speak something...")
        audio = recognizer.listen(source)

        try:
            print("🎧 Recognizing...")
            text = recognizer.recognize_google(audio)
            print("📝 You said:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Sorry, I couldn’t understand.")
            return ""
        except sr.RequestError:
            print("⚠ Could not request results. Check your internet.")
            return ""

# Run the app
spoken_text = listen()
if spoken_text:
    speak("You said " + spoken_text)