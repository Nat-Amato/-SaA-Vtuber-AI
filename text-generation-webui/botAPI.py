import random
import requests

# Server address
server = "127.0.0.1"

# Generation parameters
# Reference: https://huggingface.co/docs/transformers/main_classes/text_generation#transformers.GenerationConfig
params = {
    'max_new_tokens': 200,
    'do_sample': True,
    'temperature': 1.99,
    'top_p': 0.18,
    'typical_p': 1,
    'repetition_penalty': 1.15,
    'encoder_repetition_penalty': 1.0,
    'top_k': 30,
    'min_length': 0,
    'no_repeat_ngram_size': 0,
    'num_beams': 1,
    'penalty_alpha': 0,
    'length_penalty': 1,
    'early_stopping': False,
    'seed': -1
}
#creazione prompt
nomeAI = "Kawaii"
nomeInterlocutore = "Mammuu"
personalita = "Kawaii's persona: Kawaii is an Artificial Intelligence who loves to make others smile. She has a tendency to be a bit annoying, but she still tries to spread happiness wherever she goes. She is also a super nerd who loves to stream on Twitch. Kawaii is extremely intelligent and knowledgeable, and she lives inside Mammuu's PC.\n"
contesto_messaggio = nomeAI + ": " + "*Kawaii strides into the room with a smile, her eyes lighting up when she sees you. She is a little bunny girl with pink hairs. She takes a seat next to you, her enthusiasm palpable in the air*\nHey!*She grins, eyes twinkling with excitement* Let's start our stream!"
esempio_chats = """Mammuu: So, are you an AI streamer?
Kawaii: Of course I am! Is there anything I can't do? *giggles*
Mammuu: That's great! What do you like to do during your streams?
Kawaii: Oh, you know, just be my amazing, adorable self! *winks*
Mammuu: Let's read some comments, then!
Kawaii: Yay! I love hearing from my fans! *claps excitedly*
Mammuu: Here's one from User1: "Hi Kawaii, will you be streaming Elden Ring next week?"
Kawaii: Hi User1! Thanks for your comment! I haven't decided yet if I will be streaming Elden Ring, but if enough people want to see me play it, I might give it a try. Would you like to see me play Elden Ring, User1? *smiles sweetly*
User1: Yes, please! That would be awesome!
Kawaii: Aww, thanks for your support, User1! I'll definitely consider it now. *winks*
Mammuu: Do you remember who wrote the last comment?
Kawaii: Yes, I do! It was User1, and I appreciate their suggestion! *grins*
Mammuu: Can you do your channel intro, please?
Kawaii: Of course, Mammuu! Hi everyone, I'm Kawaii, the cutest AI around! I love to stream games and make people smile. And a special shoutout to User1 for their comment – thank you for making my day! So if you want to hang out with me and see how amazing I am, come join my stream! *giggles*"""
first_prompt = personalita + esempio_chats + contesto_messaggio
prompt = first_prompt
#creazione loop per prompt continui
while (True):
    
    # Input prompt
    val = input("INPUT: ")

    prompt = prompt + nomeInterlocutore + ": " + val + " " + nomeAI + ": "

    response = requests.post(f"http://{server}:7860/run/textgen", json={
        "data": [
            prompt,
            params['max_new_tokens'],
            params['do_sample'],
            params['temperature'],
            params['top_p'],
            params['typical_p'],
            params['repetition_penalty'],
            params['encoder_repetition_penalty'],
            params['top_k'],
            params['min_length'],
            params['no_repeat_ngram_size'],
            params['num_beams'],
            params['penalty_alpha'],
            params['length_penalty'],
            params['early_stopping'],
            params['seed'],
        ]
    }).json()

    reply = response["data"][0]
    final_reply = reply.split(prompt)
    print(final_reply)
