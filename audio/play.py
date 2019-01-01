import pyaudio
import wave
import sys
from config import *

#wrong usage of program
if len(sys.argv) < 2:   
    print ("ERROR: WRONG USAGE")
    print ("Usage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

#vars
filename = sys.argv[1]
waveFile = wave.open(filename, 'rb')
audio = pyaudio.PyAudio()
stream = audio.open( 
                    format = audio.get_format_from_width(waveFile.getsampwidth()),
                    channels = waveFile.getnchannels(),
                    rate = waveFile.getframerate(),
                    output = True 
                   )
soundData = waveFile.readframes(CHUNK)

#play
while len(soundData) > 0:
    stream.write(soundData)
    soundData = waveFile.readframes(CHUNK)

stream.stop_stream()
stream.close()

audio.terminate()
