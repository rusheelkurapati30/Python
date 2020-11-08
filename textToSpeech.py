# Python program to translate text to speech.


# from gtts import gTTS
# import os
# tts = gTTS('Good evening', lang = 'en', )
# tts.save('goodEvening1.wav')
# os.system("goodEvening1.wav")







# import winsound
# winsound.PlaySound("goodEvening.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS)

# from pydub import AudioSegment
# from pydub.playback import play

# song = AudioSegment.from_mp3("goodEvening1.wav")
# play(song)










# from playsound import playsound
# from gtts import gTTS
# enterText = input("Enter any text: ")
# tts = gTTS(enterText, lang = 'en')
# tts.save('textToSpeech1.mp3')
# playsound("textToSpeech1.mp3")









# Python program to translate text to speech.

import pyttsx3
engine = pyttsx3.init() #object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(str):
	engine.say(str)
	# engine.save_to_file(str, "tts.mp3")
	engine.runAndWait()

speak(input("\nText something: "))















# import win32com.client 
# speaker = win32com.client.Dispatch("SAPI.SpVoice") 
# s = input("Enter the word you want to speak it out by computer: ")

# def speak():
# 	speaker.Speak(s) 
  
# speak()
