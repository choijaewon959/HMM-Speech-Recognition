import pyaudio
import wave
import os
import shutil
from config import *

#vars
audio = pyaudio.PyAudio()
stream = audio.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK
)

#record
print("==========RECORDING==========")

frames = []

for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    soundData = stream.read(CHUNK)
    frames.append(soundData)

print("==========DONE RECORDING==========")

#update sound stream
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#move output file to data directory
shutil.move("output.wav", "../data")