import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data=data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Virtual Assistant")
        return "My name is Virtual Assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey, ma'am! How can I help you ?")
        return "Hey, ma'am! How can I help you ?"

    elif "goodmorning" in user_data:
        text_to_speech.text_to_speech("Good Morning")
        return "Good Morning"

    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minute:"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok maam")
        return "ok maam"

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is ready for you!")
        return "Spotify is ready for you!"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Youtube is ready for you!")
        return "Youtube is ready for you!"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Google is ready for you!")
        return "Google is ready for you!"

    elif "weather" in user_data:
        ans=weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm unable to understand your command")
        return "I'm unable to understand your command"