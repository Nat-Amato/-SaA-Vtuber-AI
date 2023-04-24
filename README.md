

# VTuber AI - Un agente informatico basato su LLM per l'assistenza in chat in streaming su YouTube: soluzione innovativa e avanzata

## Abstract

In questo progetto presentiamo un agente informatico basato su LLM progettato per fornire assistenza in tempo reale nella chat di streaming su YouTube. Descriviamo la tecnologia e l'hardware necessario per implementare questa soluzione, nonché i risultati ottenuti dai test effettuati. Oltre a fornire assistenza, questo agente può essere impiegato a scopo ludico e ricreativo. È stato progettato per rispondere alle domande degli utenti in modo efficiente e preciso, offrendo un'esperienza di streaming più coinvolgente e piacevole.

## Introduzione

Con l'aumento della popolarità delle piattaforme di streaming come YouTube, è diventato sempre più importante fornire un'assistenza efficace e un maggiore coinvolgimento agli utenti attraverso la chat. Tuttavia, gestire un gran numero di domande e richieste in tempo reale può rappresentare una sfida per gli operatori umani. Per questo motivo, abbiamo sviluppato un agente informatico basato su LLM per fornire supporto alle chat in streaming.

## Tecnologia e implementazione

I requisiti minimi hardware per l'esecuzione del nostro agente sono: 
- GPU RTX 3060ti
- CPU Intel Core i5 di 12a gen.
- RAM 16 GB
- HDD 20 GB

Lato software utilizza un Logic Learning Machine (LLM) basato su Alpaca per elaborare le domande degli utenti e fornire risposte appropriate e pertinenti in tempo reale.
La gestione delle emozioni è affidata ad un sistema di Elaborazione del Linguaggio Naturale (NLP) basato su BERT in grado di classificare i testi in cinque categorie emotive: gioia, tristezza, rabbia, paura e neutralità . 
Queste tecniche di apprendimento ed elaborazione fanno si che il nostro assistente si adatti alle esigenze degli utenti e sia in grado di offrire un'esperienza di assistenza o di semplice intrattenimento, personalizzata e di alta qualità.

## Risultati e valutazione

Il nostro sistema è stato testato e ha dimostrato di essere in grado di gestire un gran numero di domande provenienti dalla chat e fornire risposte appropriate e pertinenti in tempo reale. 
Grazie all'utilizzo di Alpaca basato su LLaMA di META, il nostro bot è in grado di fornire risposte pertinenti e tempestive. 
Inoltre, abbiamo implementato un'interfaccia umanoide per il nostro bot di streaming, che può mostrare emozioni cambiando espressione in base al contenuto delle domande degli utenti. 
Per migliorare ulteriormente l'esperienza dell'utente, il nostro bot è in grado di fornire risposte sia in formato testuale che vocale, per consentire agli utenti di scegliere il formato di risposta che preferiscono. 

## Conclusione

Concludendo, il nostro agente informatico basato su LLM rappresenta una soluzione innovativa e avanzata per fornire assistenza in chat in streaming su piattaforme come YouTube. Tuttavia, è importante notare che il bot richiede requisiti hardware avanzati per funzionare correttamente e abbiamo utilizzato la piattaforma OBS per lo streaming del nostro bot. Questa soluzione offre un'alternativa efficace alle soluzioni tradizionali basate su operatori umani e potrebbe essere estesa ad altre piattaforme di streaming e a vari contesti di assistenza online.


# Caso di studio

1. L'utente si collega alla diretta di YouTube tramite un determinato link, utilizzando il suo computer e l'accesso a internet.

2. Durante la diretta, l'utente trova il bot operativo e visibile in live, grazie all'implementazione di un'interfaccia umanoide.

3. L'utente digita una frase o una richiesta specifica nella chat di YouTube.

4. Il bot riceve la richiesta dell'utente e la elabora utilizzando tecniche avanzate di intelligenza artificiale implementate nel sistema.

5. Il bot fornisce la risposta all'utente, mostrandola a schermo e a voce mentre manifesta emozioni sul suo volto in base al contenuto del messaggio dell'utente, grazie all'utilizzo di un software di rilevamento delle emozioni e all'utilizzo di un'interfaccia umanoide.

Ricevuta la risposta del bot, sia in formato testuale che vocale, l'utente può continuare a interagire con il bot durante la diretta su YouTube.

# Repository impiegate all'interno del progetto

## Premessa
"Le repository presenti su questo account Github sono utilizzate solo a scopo didattico e di apprendimento. Se il proprietario di una repository inclusa in questo account desidera che il suo materiale venga rimosso, lo faremo immediatamente su richiesta del proprietario. Non intendiamo utilizzare o distribuire il materiale in modo non autorizzato. Tutte le repository sono soggette alle licenze e alle condizioni d'uso dei rispettivi proprietari."

## [LLM](https://en.wikipedia.org/wiki/Logic_learning_machine "LLM") (Logic Learning Machine)
Alpaca basato su LLaMA di META, in particlolare si tratta di una versione quantizzata a 4 bit di chavinlo/alpaca-native
[Link alla repository](https://huggingface.co/ozcur/alpaca-native-4bit "Link alla repository")

## Emotion Classification in Short Messages
Questa repository contiene un progetto di analisi del sentiment a più classi per classificare i testi in cinque categorie emotive: gioia, tristezza, rabbia, paura e neutralità. 
In particolare, la repository include la preparazione del dataset, l'utilizzo di machine learning tradizionale con scikit-learn, l'utilizzo di reti neurali LSTM e il transfer learning utilizzando BERT (tensorflow keras). 
In altre parole, il progetto utilizza diverse tecniche per addestrare un modello informatico a riconoscere e classificare i testi in base alle emozioni che esprimono.
[Link alla repository](https://github.com/lukasgarbas/nlp-text-emotion "Link alla repository")

## Text generation web UI
Un'interfaccia web gradio per l'esecuzione di grandi modelli linguistici come LLaMA, llama.cpp, GPT-J, Pythia, OPT e GALACTICA.
[Link alla repository](https://github.com/oobabooga/text-generation-webui "Link alla repository")

# Installazione

## Prerequisiti

### VBCABLE_Driver_Pack43.zip

Prende in input l'audio riprodotto da play.py contenuto all'interno di text-generation-webui e lo manda in output a OBS e a VSeeFace

### OBS

Prende in input VSeeFace, la sorgente virtuale VBCABLE e il file di testo reademe.text contenente la risposta del bot situato all'interno di text-generation-webui.

### VSeeFace
Contiene il VTuber umanoide da mostrare su OBS che va configurato con VBCABLE e installata la virtual camera.

## Procedimento
Download della repositoy VTuberAI.rar
eseguire il file install.bat
eseguire il file download-model.bat
scegliere un modello (nel nostro caso ozcur/alpaca-native-4bit https://huggingface.co/ozcur/alpaca-native-4bit)
eseguire il file AVVIA_SERVER.bat
verranno eseguiti 2 server:
Server_Modello_AI
e Server_Messaggi
in questo server verrà inserito il link live: che va creato avviando la diretta OBS e successivamente acquisito da youtube
dopo averlo inserito, si avvia il terzo server Server_Principale
con all'interno il gestore dei parametri
