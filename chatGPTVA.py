import speech_recognition as sr
import pyautogui
import webbrowser
import openai
import os
from gtts import gTTS
from pydub import AudioSegment
from dotenv import load_dotenv


load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY



# Get command
def listen_for_command():
   recognizer = sr.Recognizer()
   with sr.Microphone as source:
      print('Listening for commands...')
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)
      
   try:
     command = recognizer.recognize_google(audio)
     print("Google Speech Recognition thinks you said: ", command)
     return command.lower()
   
   except sr.UnkownValueError:
      print("Google Speech Recognition does not understand the audio ")
      return None
   
   except sr.RequestError as e:
       print(f"Could not request results from Google Speech Recognition service; {e}")
       return None
      

# Convert text to speech
def text_to_speech(response_text):
   print(response_text)
   tts = gTTS(text=response_text, lang="en")
   tts.save("response.mp3")
   sound = AudioSegment.from_mp3("response.mp3")
   sound.export("response.wav", format="wav")
   os.system("afplay response.wav")


def chatGPT_response(prompt):
   response = openai
      


   

