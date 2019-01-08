import pyaudio
import struct
import numpy as np 
import matplotlib.pyplot as plt
import os
import shutil
import datetime
from config import *


audio = pyaudio.PyAudio()
stream = audio.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = CHUNK
)

frames = []

for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    soundData = stream.read(CHUNK)
    frames.append(soundData)


stream.stop_stream()
stream.close()
audio.terminate()

#make wav file
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

#move output file to data directory

shutil.move("output.wav", "../data")

#convert raw sound data to specturm form
spectrum_data = b''.join(frames)
spectrum_data_int = np.array(struct.unpack(str(len(spectrum_data)) + 'B', spectrum_data), dtype = 'b')[::2] 
print(spectrum_data_int)

#plot
fig, ax = plt.subplots()
ax.plot(spectrum_data_int, '-')
x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2, -500, 500))
plt.show()

