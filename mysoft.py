import pyttsx3
import os
import speech_recognition as SRG
import time
import webbrowser
engine=pyttsx3.init()

print('''
 
 
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------

                                     *******    ********      **   **       ****** 
                                     ********      **         **  **       ********
                                     **    **      **         ** **        **    **
                                     **    **      **         ****         **    **
                                     *******       **         ****         ********
                                     **            **         ** **        **    **
                                     **            **         **  **       **    **
                                     **         ********      **   **      **    **
                                     
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------

 
''')
pyttsx3.speak("hi there you can talk with me")
print("hi there you can talk with me")
pyttsx3.speak('what do you want me to do?')


while True:
    variable = SRG.Recognizer()
    with SRG.Microphone() as source:
        print('what do you want me to do?')
        engine.runAndWait()
        
        audio_input = variable.record(source,duration=6)
        try:
            text = variable.recognize_google(audio_input)
            print(text)
        except:
            print(' Could not process audio...')
            pyttsx3.speak('Sorry Could not process audio')
            break
    if ('introduce' in text) or ('yourself' in text) :
        print('menu')
        pyttsx3.speak("myself pika your voice assistant developed by priyanka just  just tell me what do you want me to do mam")
    
    elif (("run" in text) or ("launch" in text) or ("execute"in text) or ("open" in text)) and (("notepad"in text)or("Notepad"in text)):
        pyttsx3.speak("opening notepad")
        os.system("notepad")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and (("media player"in text)or("media"in text)or("Music"in text)):
        pyttsx3.speak("opening wmplayer")
        os.system("wmplayer")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and (("chrome"in text)or("Chrome"in text)):
        pyttsx3.speak("opening chrome")
        os.system("chrome")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and (("BurpSuite"in text)or("Burp"in text)): 
        pyttsx3.speak("opening burpsuit")
        os.system("BurpSuiteCommunity")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and (("claculator"in text)or("cal"in text)): 
        pyttsx3.speak("opening claculator")
        os.system("calc")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and (("prompt"in text)or("command"in text)): 
        pyttsx3.speak("opening command prompt")
        os.system("cmd")
        
    elif(("run" in text)or("launch" in text)or("execute"in text)or("open" in text)) and ("BurpSuite"in text): 
        pyttsx3.speak("opening burpsuit")
        os.system("BurpSuiteCommunity")
        
    elif(("google" in text) or ("search" in text))and(("myself"in text)or("my name"in text)or("name")):
        pyttsx3.speak("googling  stuffs")
        webbrowser.open('https://priyankaprasad2.bookmark.com/', new = 2)
        
    elif("exit"in text)or("quit"in text):
        pyttsx3.speak("thank you i am sure developer will add more features later to me")
        break
        
    else:
        print("invalid request")
        pyttsx3.speak("command not supported ")
print()
