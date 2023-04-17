<<<<<<< HEAD
import time
import  json
import pandas as pd
import numpy as np
import subprocess
import os
import play
from getaudiodev import getaudiodevice

#05/04 simpleaudio in extensions/silero_tts/play.py. #modificato script silero per gestione nome output audio

from selenium import webdriver #da installare -- pip install seleniuim
from selenium.webdriver.chrome.service import Service # -- pip install webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from chat_downloader import ChatDownloader #da installare -- pip install chat-downloader

from os import system
system("title " + "Server")
 
##Avvio modello Emozioni
import ktrain #da installare -- pip install ktrain
from ktrain import text
predictor = ktrain.load_predictor('./models_Emo/bert_model')
model = ktrain.get_predictor(predictor.model, predictor.preproc)

##Avvio pagina chrome per controllo Kawaii
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:7860/")

def invio_messaggio(userinput):
    #driver.find_element cerca i tasti o le caselle di testo nella pagina chrome aperta
    text_gen = driver.find_element(By.CSS_SELECTOR, "body > gradio-app:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    text_gen.click() #riporta su scheda chat (in caso modifico parametri e mi dimentico di tornare a scheda chat)
    generate = driver.find_element(By.ID, 'component-6')
    textbox = driver.find_element(By.CSS_SELECTOR, "div[id='component-4'] textarea[class='scroll-hide svelte-4xt1ch']")
    textbox.send_keys(userinput)
    generate.click()

def selenium_send(userinput):
    # ️ using find_element method to search last message from bot, generate button and textarea.
    separatore = "</audio><br><br>"
    controllo = "Is recording a voice message"

    invio_messaggio(userinput)
    time.sleep(1) #oe attento! selenium legge veloce
    with open('readme.txt', 'w') as f:
        f.write("")
    messaggibot = driver.find_element(By.CSS_SELECTOR, ".message.bot.svelte-6roggh.latest")
    testobot = messaggibot.get_attribute("innerHTML")
     #controllo se il bot sta ancora scrivendo la risposta precedente
    while (testobot.find(controllo) != -1):
        messaggibot = driver.find_element(By.CSS_SELECTOR, ".message.bot.svelte-6roggh.latest")
        testobot = messaggibot.get_attribute("innerHTML")    
    #separo la risposta per prendere solo il messaggio, nella versione con TTS, nel messaggio intero è incluso anche l'import del messaggio vocale
    text = testobot.split('</audio><br><br>')
    import re

    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text_noemoji = emoji_pattern.sub(r'', text[1]) # no emoji
    print(text[1])
    start_time = time.time() 
    prediction = model.predict(text[1])
        #scrive risposta su file txt per essere inserita in overlay obs

    print(prediction)

    #scrive risposta su file txt per essere inserita in overlay obs
    with open('readme.txt', 'w', encoding='utf8') as f:

        f.write(text_noemoji)
        f.write('\n')
        testobot = controllo

    #avvia audio risposta
    #subprocess.call('start play.py ' + prediction, shell=True)
    filename = './extensions/silero_tts/outputs/messvocale.wav'
    play.voiceandface(prediction, filename, device) #filename = percorso+ nome file audio


userinput_old = ""
with open('readme.txt', 'w') as f:
    f.write("")
device = getaudiodevice()
while(True):
    time.sleep(1)
    f = open('Output.json')
    data = json.load(f)
    last_text = data[-1]
    author = last_text['author']['name']
    message = last_text['message']    
    userinput = '"' + author + ': ' + message +'"'
    f.close()
    if(userinput != userinput_old):
        print(userinput)
        selenium_send(userinput)
        userinput_old = userinput



=======
import time
import  json
import pandas as pd
import numpy as np
import subprocess
import os
import play
from getaudiodev import getaudiodevice

#05/04 simpleaudio in extensions/silero_tts/play.py. #modificato script silero per gestione nome output audio

from selenium import webdriver #da installare -- pip install seleniuim
from selenium.webdriver.chrome.service import Service # -- pip install webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from chat_downloader import ChatDownloader #da installare -- pip install chat-downloader

from os import system
system("title " + "Server")
 
##Avvio modello Emozioni
import ktrain #da installare -- pip install ktrain
from ktrain import text
predictor = ktrain.load_predictor('./models_Emo/bert_model')
model = ktrain.get_predictor(predictor.model, predictor.preproc)

##Avvio pagina chrome per controllo Kawaii
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:7860/")

def invio_messaggio(userinput):
    #driver.find_element cerca i tasti o le caselle di testo nella pagina chrome aperta
    text_gen = driver.find_element(By.CSS_SELECTOR, "body > gradio-app:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    text_gen.click() #riporta su scheda chat (in caso modifico parametri e mi dimentico di tornare a scheda chat)
    generate = driver.find_element(By.ID, 'component-6')
    textbox = driver.find_element(By.CSS_SELECTOR, "div[id='component-4'] textarea[class='scroll-hide svelte-4xt1ch']")
    textbox.send_keys(userinput)
    generate.click()

def selenium_send(userinput):
    # ️ using find_element method to search last message from bot, generate button and textarea.
    separatore = "</audio><br><br>"
    controllo = "Is recording a voice message"

    invio_messaggio(userinput)
    time.sleep(1) #oe attento! selenium legge veloce
    with open('readme.txt', 'w') as f:
        f.write("")
    messaggibot = driver.find_element(By.CSS_SELECTOR, ".message.bot.svelte-6roggh.latest")
    testobot = messaggibot.get_attribute("innerHTML")
     #controllo se il bot sta ancora scrivendo la risposta precedente
    while (testobot.find(controllo) != -1):
        messaggibot = driver.find_element(By.CSS_SELECTOR, ".message.bot.svelte-6roggh.latest")
        testobot = messaggibot.get_attribute("innerHTML")    
    #separo la risposta per prendere solo il messaggio, nella versione con TTS, nel messaggio intero è incluso anche l'import del messaggio vocale
    text = testobot.split('</audio><br><br>')
    import re

    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text_noemoji = emoji_pattern.sub(r'', text[1]) # no emoji
    print(text[1])
    start_time = time.time() 
    prediction = model.predict(text[1])
        #scrive risposta su file txt per essere inserita in overlay obs

    print(prediction)

    #scrive risposta su file txt per essere inserita in overlay obs
    with open('readme.txt', 'w', encoding='utf8') as f:

        f.write(text_noemoji)
        f.write('\n')
        testobot = controllo

    #avvia audio risposta
    #subprocess.call('start play.py ' + prediction, shell=True)
    filename = './extensions/silero_tts/outputs/messvocale.wav'
    play.voiceandface(prediction, filename, device) #filename = percorso+ nome file audio


userinput_old = ""
with open('readme.txt', 'w') as f:
    f.write("")
device = getaudiodevice()
while(True):
    time.sleep(1)
    f = open('Output.json')
    data = json.load(f)
    last_text = data[-1]
    author = last_text['author']['name']
    message = last_text['message']    
    userinput = '"' + author + ': ' + message +'"'
    f.close()
    if(userinput != userinput_old):
        print(userinput)
        selenium_send(userinput)
        userinput_old = userinput



>>>>>>> 8ec1b3b23fd208bbc10254d88e9a27f303f25ba7
