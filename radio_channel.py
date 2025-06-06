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
class Visualizer:
    @staticmethod
    def plot_signal(time, signal, title="Signal"):
        plt.figure(figsize=(10, 4))
        plt.plot(time, signal)
        plt.title(title)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
    
    @staticmethod
    def save_plot(time, signal, filename="signal.png"):
        plt.figure(figsize=(10, 4))
        plt.plot(time, signal)
        plt.savefig(filename)
        plt.close()
    
    @staticmethod
    def add_noise(signal, noise_level=0.1):
        noise = np.random.normal(0, noise_level, signal.shape)
        return signal + noise
```

**5.4.3 Основной скрипт**  
```python
# simulation.py
from radio_channel import SignalGenerator, Modulator, Visualizer
import numpy as np

# Параметры сигнала
fs = 44100  # Частота дискретизации (Гц)
duration = 0.5  # Длительность (с)
t = np.linspace(0, duration, int(fs * duration))

# Генерация сигнала
gen = SignalGenerator(frequency=440, amplitude=0.8)
signal = gen.generate(t)

# Модуляция
modulator = Modulator(carrier_frequency=5000)
am_signal = modulator.am_modulate(signal, t)
fm_signal = modulator.fm_modulate(signal, t, modulation_index=5.0)

# Визуализация
viz = Visualizer()
viz.plot_signal(t, signal, "Original Signal")
viz.plot_signal(t, am_signal, "AM Modulated")
viz.plot_signal(t, fm_signal, "FM Modulated")

# Добавление шума и сохранение
noisy_signal = viz.add_noise(am_signal, noise_level=0.3)
viz.save_plot(t, noisy_signal, "am_noisy.png")
