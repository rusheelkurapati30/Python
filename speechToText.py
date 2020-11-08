# Python program to translate speech to text.

import speech_recognition as sr
# import pyaudio
r = sr.Recognizer()
print("\nPlease Talk: ")
with sr.Microphone() as source: 
	audio_data = r.record(source, duration = 3)
	print("\nRecognizing...")

try: 
	text = r.recognize_google(audio_data)
	print("\nYou said : " + text)
except:
	print("\nSorry could not recognize your voice.")

with open("recorded.wav", "wb") as f:
	f.write(audio_data.get_wav_data())











 
# import speech_recognition as sr 
# import pyttsx3  
# import pyaudio
  
# # # Initialize the recognizer  
# r = sr.Recognizer()  
  
# # # Function to convert text to 
# # # speech 
# def SpeakText(command): 
      
# #     # Initialize the engine 
#     engine = pyttsx3.init() 
#     engine.say(command)  
#     engine.runAndWait() 
      
      
# # # Loop infinitely for user to 
# # # speak 
  
# while(1):     
#     try: 
#     	print("Please Talk: ")
#         with sr.Microphone() as source2: 
#             r.adjust_for_ambient_noise(source2, duration=0.2) 
#             audio2 = r.listen(source2) 
#             MyText = r.recognize_google(audio2) 
#             MyText = MyText.lower() 
  
#             print("Did you say "+MyText) 
#             SpeakText(MyText) 
              
#     except sr.RequestError as e: 
#         print("Could not request results; {0}".format(e)) 
          
#     except sr.UnknownValueError: 
#         print("unknown error occured") 