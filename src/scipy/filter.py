
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    b, a = signal.butter(8, 0.02, 'highpass')
    data = [math.sin(i / 10.0) for i in range(50)]
    filtedData = signal.filtfilt(b, a, data) #data为要过滤的信号
    print(filtedData)

    b, a = signal.butter(4, 100, 'low', analog=True)
    w, h = signal.freqs(b, a)
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('Butterworth filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(100, color='green') # cutoff frequency
    plt.show()
    
