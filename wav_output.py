import numpy as np
import wave

w = wave.Wave_write("/home/pi/Music/ohayo.wav")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
w.writeframes(x)
w.close()
