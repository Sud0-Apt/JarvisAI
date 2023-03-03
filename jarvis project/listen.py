# googletrans and speech_recognition module for import
# 1. function to listen
# 2. function for convertion of language
# 3. function to print the voice

# import speech_recognition as sr
# from googletrans import Translator

# #1 listen
# def Listen():
#     s = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening")
#         s.pause_threshold = 0.7
#         audio = s.listen(source,0,7)

#         try:
#             print("recognizing")
#             query = s.recognize_google(audio,language="hi")
         

#         except:
#             print("Try again...")

#     return query          

# Listen()

# def convert_hi_en():

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
# 1 - Listen : Hindi or English
# def Listen ():
#     r = sr. Recognizer()
#     with sr.Microphone () as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen (source, 0,8) # Listening Mode.....
#     try:
#         print("Recognizing...")
#         query = r. recognize_google(audio, language="kn")
#     except:
#         return ""
#         query = str(query).lower ()
#     return query
#Listen()

# print(Listen())

def translateHinToEng(text):
    line = str(text)
    transalte = Translator()
    result = transalte.translate(line)
    data = result.text
    print(f"you : {data}")
    return data

translateHinToEng("ಹೇಗ್ ಇದ್ದೀಯ")