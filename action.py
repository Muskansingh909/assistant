import text_to_speech

import speech_text
import datetime
import webbrowser

def action(data):
    user_data=data.lower()

    if"what is your name "in user_data:
        text_to_speech.text_to_speech("my name is virtual assistant")
        return "MY name is virtual assistant"

    elif "hello"in user_data or "hye"in user_data:
        text_to_speech.text_to_speech("hey,mam how can i help you")

    elif "time now"in user_data :
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minute"

        speech_text.speech_text("time")

    elif"shutdown"in user_data:
        text_to_speech.text_to_speech("oh mam")

    elif"play music"in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is ready")

    elif"open youtube"in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is ready")


    elif"open google"in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is ready")








