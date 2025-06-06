# radio_channel.py
import numpy as np
import matplotlib.pyplot as plt

class SignalGenerator:
    def __init__(self, frequency, amplitude=1.0):
        self.frequency = frequency
        self.amplitude = amplitude
        
    def generate(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)

class Modulator:
    def __init__(self, carrier_frequency):
        self.carrier_frequency = carrier_frequency
        
    def am_modulate(self, signal, time):
        carrier = np.sin(2 * np.pi * self.carrier_frequency * time)
        return (1 + signal) * carrier
        
    def fm_modulate(self, signal, time, modulation_index=1.0):
        phase = 2 * np.pi * self.carrier_frequency * time + modulation_index * signal
        return np.sin(phase)
