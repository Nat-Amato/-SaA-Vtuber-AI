from chat_downloader import ChatDownloader

url = input("Inserisci link live: ")
chat = ChatDownloader().get_chat(url, output="./Output.json")       # create a generator
for message in chat:                        # iterate over messages
    #chat.print_formatted(message) # print the formatted message
    # Analizza la stringa JSON e ottiene l'autore e il contenuto del messaggio
    author = message['author']['name']
    message = message['message']    
    userinput = '"' + author + ': ' + message +'"'
    print(userinput)





