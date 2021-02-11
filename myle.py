import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyaudio
import smtplib
import pyautogui
import requests
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
enigne = engine.setProperty("voice", voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon.")
    else:
        speak("Good Evening.")

    speak("How can I help you sir?")


def takeCommand():
    """[summary]
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening.")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing.")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again...")
        speak("Say that again please.")
        return "Null"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("jinesh.170670107030@gmail.com",
                 "KILLEDbyCOOKIE747")  # READ PASSWORD FROM FILE
    server.sendmail("jinesh.170670107030@gmail.com", to, content)
    server.close()


def weather():
    speak("Which city?")
    city = takeCommand().lower()
    apiAddress = ("https://api.openweathermap.org/data/2.5/weather?q=" + city +
                  "&appid=9530c17bc295116e09171bdceffe79cb")
    w = requests.get(apiAddress).json()
    w2 = round(w["main"]["temp"] / 10)
    w3 = w["weather"][0]["description"]
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 30)
    speak("Currently in" + city + "it is" + str(w2) + "degree celcius, and" +
          w3)
    engine.setProperty("rate", rate + 30)


def tinder():
    edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    os.startfile(edgePath)
    pyautogui.PAUSE = 1.5
    pyautogui.moveTo(1353, 101)  # searchbar edge Point(x=1353, y=101)
    pyautogui.click(1353, 101)  # searchbar edge
    pyautogui.PAUSE = 0
    pyautogui.typewrite("https://tinder.com/app/recs")
    pyautogui.PAUSE = 1.5
    pyautogui.press('enter')
    

    while True:
        try:
            query = takeCommand().lower()
            print(f"User Said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            speak("Say that again please.")
            return "None"
        return query

def openBrowser(url):
    url = url
    options = Options()
    options.add_argument('user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(options=options)
    driver.get("https://" + url)

    if url == "amazon.in":
        speak = ("What would you like to search on Amazon?")
        x = takeCommand().lower()
        #while True:
        #    try:
        #        x = takeCommand().lower()
        #        print(f"User Said: {x}\n")
        #    except Exception as e:
        #        print("Sorry you did not tell me what to search.")
        #        speak("Sorry you did not tell me what to search.")
        #        return "None"
        #    return x
        searchbox = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[3]/div[1]/input')
        searchbox.send_keys(x)
        searchbutton = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
        searchbutton.click()

if __name__ == "__main__":
    wish()  # get random choise from greetre
    while True:
        query = takeCommand().lower()

        # logic

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.in")
        elif "open amazon" in query:
            webbrowser.open("amazon.in")
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            songsDir = "D:\\Work\\Aura\\Songs"
            songs = os.listdir(songsDir)
            print(songs)
            os.startfile(os.path.join(songsDir,
                                      songs[0]))  # random music remaining

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is, " + strTime)

        elif "open code" in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:  # make dict key=name value=email
            try:
                speak("What should I say?")
                mailContent = takeCommand()
                to = "j08012000d@gmail.com"
                sendEmail(to, mailContent)
                speak("Email sent.")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email at the moment.")

        elif "exit" in query:
            exit()

        elif "search on web" in query:
            speak("What would you like to search sir?")
            url = takeCommand().lower()
            openBrowser(url)
            #edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            #os.startfile(edgePath)
            #pyautogui.PAUSE = 1.5
            #pyautogui.moveTo(1353, 101)  # searchbar edge Point(x=1353, y=101)
            #pyautogui.click(1353, 101)  # searchbar edge
            #pyautogui.PAUSE = 0
            #pyautogui.typewrite(url)
            #pyautogui.PAUSE = 1.5
            #pyautogui.press('enter')

        elif "close tab" in query:
            pyautogui.click(287, 60)  # close tab Point(x=287, y=60)

        elif "weather" in query:
            weather()

        elif "joke" in query:
            rate = engine.getProperty("rate")
            engine.setProperty("rate", rate - 30)
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            engine.setProperty("rate", rate + 30)
        elif "not funny" in query:
            speak("Well. you are the one who created me.")

        elif "facebook messenger" in query:
            edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(edgePath)
            pyautogui.PAUSE = 1.5
            pyautogui.moveTo(1353, 101)  # searchbar edge Point(x=1353, y=101)
            pyautogui.click(1353, 101)  # searchbar edge
            pyautogui.PAUSE = 0
            pyautogui.typewrite("https://www.facebook.com/messages/t/")
            pyautogui.PAUSE = 1.5
            pyautogui.press('enter')

        elif "tinder" in query:
            tinder()

        elif "yes" in query:
            pyautogui.press("right")

        elif "no" in query:
            pyautogui.press("left")

        elif "mailbox" in query:
            edgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(edgePath)
            pyautogui.PAUSE = 1.5
            pyautogui.moveTo(1353, 101)  # searchbar edge Point(x=1353, y=101)
            pyautogui.click(1353, 101)  # searchbar edge
            pyautogui.PAUSE = 0
            pyautogui.typewrite("mail.google.com")
            pyautogui.PAUSE = 1.5
            pyautogui.press('enter')

        elif "amazon" in query:
            openBrowser("amazon.in")

        elif "whatsapp" in query:
            i = True
            while i == True:    
                speak("Whom do you want to send message?")
                r = takeCommand().lower()
                print("User Said: " + r)
                speak("Whats the message?")
                m = takeCommand().lower()
                print("User Said: " + m)
                url = "web.whatsapp.com"
                options = Options()
                options.add_argument('user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data')
                driver = webdriver.Chrome(options=options)
                driver.get("https://" + url)
                time.sleep(10)
                search = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
                search.send_keys(r)
                time.sleep(2)
                search.send_keys(Keys.ENTER)
                message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
                message.send_keys(m)
                time.sleep(2)
                message.send_keys(Keys.ENTER)

                speak("Do you want to send another message?")
                choice = takeCommand().lower()
                if choice == "no":
                    i = False
