er#importing speech recognition library
import speech_recognition as sr 
from textblob import TextBlob
import nltk as nl
#importing OS
import os 
import logging
  
#importing AudioSegment for audio chunks
from pydub import AudioSegment 
#importing split_on_silence for splitting the audio
from pydub.silence import split_on_silence 

#creating recognizer
import speech_recognition as sr
sr.__version__
r = sr.Recognizer()

def harvard():
    #using record to capture data from an audio file
    audio_file = sr.AudioFile('harvard.wav')
    
    #using google recognizer to recognize the audio file (harvard.wav)
    with audio_file as source:
        audio = r.record(source)
        google_output = r.recognize_google(audio)
        return google_output, len(google_output)

def OSR_us_000_0010_8k():
        
    audio_file = sr.AudioFile('OSR_us_000_0010_8k.wav')
    #using google recognizer to recognize the audio file (OSR_us_000_0010_8k.wav)
    with audio_file as source:
        audio = r.record(source)
        text_output = r.recognize_google(audio)
        print(text_output)
        print(len(text_output))
        
def cut_2019_10_30_16_52_02():
        
    audio_file = sr.AudioFile('cut_2019_10_30_16_52_02.wav')
    #Danish language
    #using google recognizer to recognize the audio file (2019_10_30_16_52_02.wav)
    with audio_file as source:
        audio = r.record(source)
        google_output = r.recognize_google(audio, language = "da-DK")
        return google_output, len(google_output)

def fun_22():
    audio_file = sr.AudioFile('22.wav')
    #Danish language
    #using google recognizer to recognize the audio file (2019_10_30_16_52_02.wav)
    with audio_file as source:
        #This method is to reduce the effect of noise and we can give it a duration
        r.adjust_for_ambient_noise(source, duration=0.5)
        #The record method is to capture from the source file
        audio = r.record(source)
        '''
        if we want to capture until the fourth second we can use
        audio = r.record(source, duration=4)
        if we want to ignore a number of seconds we can use the offset
        audio = r.record(source, offset=4, duration=3)
        '''
        
        #Now this is the recognizer method, which could be google, IBM, or others
        google_output = r.recognize_google(audio, language = "da-DK", show_all=True)
        return google_output, len(google_output)
def brug(duration):
        
    audio_file = sr.AudioFile('brug-af-person data2.wav')
    with audio_file as source:
        #This method is to reduce the effect of noise and we can give it a duration
        r.adjust_for_ambient_noise(source, duration=0.1)
        #The record method is to capture from the source file
        audio = r.record(source)
        #Now this is the recognizer method, which could be google, IBM, or others
        google_output = r.recognize_google(audio, language = "da-DK")
        return google_output, len(google_output)

if __name__ == '__main__':
    durations = [0.1]
    with open('result.txt','w+') as result:
        for duration in durations:
            text, length = brug(duration)
            result.write('The transcribed text is: \n ' + text + '\n' + 'The duration is: '+str(duration) + '\n')
            result.write('The length of the text is: ' + str(length) + '\n \n')
            logging.info(duration)
#Reference: https://realpython.com/python-speech-recognition/