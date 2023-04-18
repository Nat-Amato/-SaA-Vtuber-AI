import os
import time
import wave
import pyautogui #da installare -- pip install pyautoguy
import sounddevice as sd  #pip install sounddevice
import soundfile as sf  #pip install pysoundfile
import logging
#prediction = emotion
'''
def voiceandface(prediction):
    set_face(prediction)
    wave_read = wave.open('./extensions/silero_tts/outputs/messvocale.wav', 'rb')
    wave_obj = sa.WaveObject.from_wave_read(wave_read)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    time.sleep(1)
    set_default_face()
'''

def voiceandface(prediction, filename, device):
    set_face(prediction)
    print("hey!")
    play_audio(filename = filename, device = device)
    time.sleep(1)
    set_default_face()

def set_face(prediction):
    if(prediction == 'joy') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f4')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f2')
             
    elif(prediction == 'sadness') :
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f5")
        pyautogui.keyUp("f5")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")
    elif(prediction == 'fear') :
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f6")
        pyautogui.keyUp("f6")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl") 
    elif(prediction == 'anger') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f3')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f3')

    elif(prediction == "neutral"):
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f1")
        pyautogui.keyUp("f1")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")

def set_default_face():
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f1")
        pyautogui.keyUp("f1")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")




def play_audio(filename, device):
    try:
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs, device=device, blocking=True)
        status = sd.get_status()
        if status:
            logging.warning(str(status))
        sd.wait()
    except KeyboardInterrupt:
        print('\nInterrupted by user')
    except Exception as e:
        print(type(e)._name_ + ': ' + str(e))

