import pyaudio
from config import *

#vars
audio = pyaudio.PyAudio()
stream = audio.open(
    format = audio.get_format_from_width(WIDTH),
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)

print("==========RECORDING==========")
for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    soundData = stream.read(CHUNK)
    stream.write(soundData, CHUNK)

print("==========DONE RECORDING==========")

stream.stop_stream()
stream.close()
audio.terminate()
