from textblob import TextBlob
import nltk
import pyaudio as py
import logging
import speech_recognition as sr 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#Creating a recognizer
r = sr.Recognizer()

#The list of the default microphone devices
pa = py.PyAudio()
microphone_index = pa.get_default_input_device_info()['index']

#Defining the microphone
mic = sr.Microphone(device_index=microphone_index)

#Listening through the mic (recognizng english language)
def recognize_english():
    with mic as source:
        logger.info('listening >>>>>')
        #uncomment the line below if there's noise
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    logger.info('end of speech, translating >>>>>')
    text = r.recognize_google(audio)
    return text

#Listening through the mic (recognizng danish language)
def recognize_danish():
    with mic as source:
        logger.info('listening >>>>>')
        #uncomment the line below if there's noise
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = r.recognize_google(audio, language = "da-DK")
    return text

#Analyzing the text sentiment
def analyze_text(text, language):
    if language == "da":
        text = text.translate(from_lang="da", to='en')
        
    textblob_text = TextBlob(text)
    if textblob_text.sentiment.polarity < 0:
        sentiment = "Negative"
    elif textblob_text.sentiment.polarity > 0:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"
    return textblob_text.sentiment, sentiment


if __name__ == '__main__':
    transcribed_text = recognize_english()
    sentiment = analyze_text(transcribed_text, "en")
    print(f'Text is: {transcribed_text}')
    logger.info('Showing sentiment result >>>>>>')
    print(f'The sentiment result is: {sentiment}')


