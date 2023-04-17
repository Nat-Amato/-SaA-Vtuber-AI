<<<<<<< HEAD
import sounddevice as sd
#print(sd.query_devices())
def getaudiodevice():
    devices = sd.query_devices()
    for i in devices:
        if "CABLE Input (VB-Audio Virtual Cable)" in i['name']:
            if (i['hostapi'] == 3):
                return i['index']

=======
import sounddevice as sd
#print(sd.query_devices())
def getaudiodevice():
    devices = sd.query_devices()
    for i in devices:
        if "CABLE Input (VB-Audio Virtual Cable)" in i['name']:
            if (i['hostapi'] == 3):
                return i['index']

>>>>>>> 8ec1b3b23fd208bbc10254d88e9a27f303f25ba7
