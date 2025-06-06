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

4. Работа с Git 
5.5.1-5.5.3 Ветвление и коммиты:
git checkout -b feature/am-fm-modulation
git add .
git commit -m "Добавлены AM/FM модуляция"
git push origin feature/am-fm-modulation

git checkout -b feature/visualization
git add .
git commit -m "Класс визуализации + сохранение в файл"
git push origin feature/visualization

git checkout -b feature/noise
git add .
git commit -m "Добавление гауссовского шума"
git push origin feature/noise

# Слияние с main
git checkout main
git merge feature/am-fm-modulation
git merge feature/visualization
git merge feature/noise
git push origin main
