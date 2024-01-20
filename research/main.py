import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import datetime
import os
import sys
from pygame import mixer
import time

engine = pyttsx3.init('sapi5')
mixer.init()


en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"  # female
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"  # male

engine.setProperty('voice', ru_voice_id)


def talk_function(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greeting_function():

    currentHour = int(datetime.datetime.now().hour)
    if currentHour >= 0 and currentHour < 12:
        talk_function('Good Morning!')

    if currentHour >= 12 and currentHour < 18:
        talk_function('Good Afternoon!')

    if currentHour >= 18 and currentHour !=0:
        talk_function('Good Evening!')

greeting_function()

talk_function('Hello, I am your digital assistant!. My name is delta')
talk_function('How may I help you?')

email_spell_mistake = 0

def email_spell():

    global email_spell_mistake

    query = ""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        mixer.music.load('sound-effects/sound0.mp3')
        mixer.music.play()
        time.sleep(0)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        email_mis = ["Sorry, I can't hear you. Spell the email address properly." ,"Spell the email address properly.","Sorry, Spell your email address correctly"]
        talk_function(random.choice(email_mis))
        email_spell_mistake = email_spell_mistake + 1

        if email_spell_mistake == 3:
            res = ["Sorry, I can't send you email for you. You are spelling the email address incorrectly.","I can't send you email for you. try again later. Because,  you are spelling incorrectly"]
            talk_function(random.choice(res))
        else:
            email_spell()

    return query


email_content_mistake = 0 

def email_content():

    global email_content_mistake

    query = ""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        mixer.music.load('sound-effects/sound0.mp3')
        mixer.music.play()
        time.sleep(0)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        talk_function(random.choice(Statements.Robot_Activation_Statements_cant_hear))
        email_content_mistake = email_content_mistake + 1

        if email_content_mistake == 3:
            res = ["Sorry, I can't send you email for you. You are not telling the content of the email.","I can't send you email for you. try again later. Because,  you are telling incorrectly"]
            talk_function(random.choice(res))
        else:
            email_content()

    return query

def send_mail_function():
    questions = ["Okay!. Can you please, spell me the recipient's email address. Spell me, do not tell me the address at once.","Sure, Spell me the recipient's email address. Spell me"]
    talk_function(random.choice(questions))
    recipientEmail =  email_spell()

    recipientEmail = "".join(recipientEmail.split())
    recipientEmail = recipientEmail.lower()

    try:
        message_res = ["What should I say? ","Tell me the message"]
        talk_function(random.choice(message_res))
        content = email_content()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("machinealpha9@gmail.com", 'machinealpha123456789')
        server.sendmail('machinealpha9@gmail.com', recipientEmail , content)
        print("sent to {}".format(recipientEmail))

        server.close()
        talk_message = ["Email was sent!","The email was sent successfully."] 
        talk_function(random.choice(talk_message))

    except:
        res = ['Sorry!, I am unable to send your message at this moment!',"Something went wrong. I can't send the email right now"]
        talk_function(random.choice(res))

    
def myCommand():
   
    r = sr.Recognizer() 
    query = ""                                                                                  
    with sr.Microphone() as source: 
        mixer.music.load('sound-effects/sound0.mp3')
        mixer.music.play()                                                                      
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
    	pass

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query or 'start youtube' in query or 'launch youtube' in query :
           
            resYou = ["Okay. youtube is opening","okay. youtube is launching","sure, youtube is starting"]
            talk_function(random.choice(resYou))
            webbrowser.open('www.youtube.com')

        elif 'open google' in query or 'start google' in query or 'launch google' in query:
           
            resGoogle = ["Okay. google is opening","okay. google is launching","sure, google is starting"]
            talk_function(random.choice(resGoogle))
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query or 'start gmail' in query or 'launch gmail' in query:
            
            resGmail = ["Okay. gmail is opening","okay. gmail is launching","sure, gmail is starting"]
            talk_function(random.choice(resGmail))
            webbrowser.open('www.gmail.com')
        
        elif 'open facebook' in query or 'start facebook' in query or 'launch facebook' in query:

        	resfb = ["Okay. facebook is opening","okay. facebook is launching","sure, facebook is starting"]
        	talk_function(random.choice(resfb))
        	webbrowser.open('www.facebook.com')

        elif 'send an email' in query or 'send email' in query or 'send mail' in query or 'send a mail' in query:
            send_mail_function()


        elif 'deactivate delta' in query or 'deactivate' in query or 'stop' in query:
            talk_function('okay')
            talk_function('Bye, have a good day. I am going offline')
            sys.exit()

        elif 'bye' in query:
            talk_function('Bye, have a good day. i am going offline')
            sys.exit()
                                    
        elif 'play music' in query or 'start music' in query:
            
            music = ["music1.mp3","music2.mp3","music3.mp3","music4.mp3","music5.mp3"]
            os.system(random.choice(music))
            talk_function('Okay, here is your music! Enjoy!')

        elif 'open my computer' in query or 'open computer' in query or 'launch computer' in query:
        	
        	resfb = ["Okay. My computer is opening","okay. This pc is launching","sure, the computer is starting"]
        	talk_function(random.choice(resfb))
        	os.system("thispc.exe")

       	elif "open notepad" in query or "launch notepad" in query or 'start notepad' in query:
       		
       		resfb = ["Okay. The notepad is opening","okay. The notepad is launching","sure, the notepad is starting"]
       		talk_function(random.choice(resfb))
       		os.system("note.exe")

       	elif "open word" in query or "launch word" in query or 'start word' in query:
       		resfb = ["Okay. The word is opening","okay. The word is launching","sure, the word is starting"]
       		talk_function(random.choice(resfb))
       		os.system("word.exe")


       	elif "open excel" in query or "launch excel" in query or 'start excel' in query:
       		resfb = ["Okay. The excel is opening","okay. The excel is launching","sure, the excel is starting"]
       		talk_function(random.choice(resfb))
       		os.system("excel.exe")

       	elif "open power point" in query or "launch power point" in query or 'start power point' in query:
       		resfb = ["Okay. The power point is opening","okay. The power point is launching","sure, the power point is starting"]
       		talk_function(random.choice(resfb))
       		os.system("power.exe")

       	elif "open google chrome" in query or "launch google chrome" in query or 'open chrome' in query:
       		resfb = ["Okay. The chrome point is opening","okay. The chrome point is launching","sure, the chrome point is starting"]
       		talk_function(random.choice(resfb))
       		os.system("chorome.exe")
       		
        else:
        	pass
        	print("pass")

        nextRes = ["Next Command!","what can i do next", "tell me what to do next"]
        talk_function(random.choice(nextRes))
        
