import random
import datetime
import webbrowser


class Controller:
    def __init__(self):
        pass

    def control(query):
        if query in ['open youtube', 'start youtube', 'launch youtube']:
            webbrowser.open("https://www.youtube.com")
            return "Okay, I am opening YouTube."
        
        elif query in ["open google", "start google", "launch google"]:
            webbrowser.open("https://www.google.com")
            return "Okay, I am opening google."
        
        elif query in ["open gmail", "start gmail", "launch gmail"]:
            webbrowser.open("https://mail.google.com/")
            return "Okay, I am opening gmail."

        elif query in ["open facebook", "launch facebook", "start facebook"]:
            webbrowser.open("https://mail.facebook.com/")
            return "Okay, I am opening facebook."

        elif query in ["open linkedin", "launch linkedin", "start linkedin"]:
            webbrowser.open("https://www.linkedin.com/")
            return "Okay, I am opening Linkedin."

        elif query in ["open instagram", "open insta", "launch instagram", "launch insta"]:
            webbrowser.open("https://www.instagram.com/")
            return "Okay, I am opening instagram."

        elif query in ["open x", "launch x", "start x"]:
            webbrowser.open("https://twitter.com/")
            return "Okay, I am opening x."

        elif query in ["open tiktok", "launch tiktok", "start tiktok"]:
            webbrowser.open("https://www.tiktok.com/")
            return "Okay, I am opening tiktok."

        elif query in ["open github", "launch github", "start github"]:
            webbrowser.open("https://www.github.com/")
            return "Okay, I am opening github."

        else:
            return "[NONE]"



       