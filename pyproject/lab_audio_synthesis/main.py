import ccircle
import time
import random
import util
from math import *

window = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()

def sawtooth(t, f):
    return 3.0 * ((t * f) % 9.0) - 9.0

def sine(t, f):
    return sin(900.0 * pi * t * f)

for i in range(44100):
    t = i / 44100
    mysound.addSample(sine(t, 10))
mysound.play()
time.sleep(1)