from chat_downloader import ChatDownloader
import subprocess

from os import system
system("title " + "Server_Messaggi")

url = input("Inserisci link live: ")
chat = ChatDownloader().get_chat(url, output="./Output.json")       # create a generator
subprocess.Popen(["start", "cmd", "/k", "python", "SELENIUMGPT_Emo.py"], shell=True)
for message in chat:                        # iterate over messages
    #chat.print_formatted(message) # print the formatted message
    # Analizza la stringa JSON e ottiene l'autore e il contenuto del messaggio
    author = message['author']['name']
    message = message['message']    
    userinput = '"' + author + ': ' + message +'"'
    print(userinput)





