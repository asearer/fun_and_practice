import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def detect_satellite_signal(signal, threshold=0.5, peak_distance=100):
    """
    Detect satellite signals in a given signal.

    Args:
    - signal (array-like): The input signal.
    - threshold (float): Threshold for peak detection.
    - peak_distance (int): Minimum peak distance.

    Returns:
    - peaks (array): Indices of detected peaks.
    """
    
    # Find peaks in the signal
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)
    
    return peaks

# Example usage:
if __name__ == "__main__":
    # Generate a synthetic satellite signal
    time = np.linspace(0, 10, 1000)
    signal = np.sin(2 * np.pi * 2 * time) + 0.5 * np.sin(2 * np.pi * 5 * time)
    
    # Add noise to the signal
    noise = np.random.normal(0, 0.2, signal.shape)
    noisy_signal = signal + noise
    
    # Detect satellite signals
    detected_peaks = detect_satellite_signal(noisy_signal)
    
    # Plot the original signal and detected peaks
    plt.plot(time, noisy_signal, label='Noisy Signal')
    plt.plot(time[detected_peaks], noisy_signal[detected_peaks], 'x', color='red', label='Detected Peaks')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Satellite Signal Detection')
    plt.legend()
    plt.grid(True)
    plt.show()
