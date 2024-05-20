# signal_processing.py
import numpy as np
from scipy.signal import find_peaks
from scipy.fft import fft

def detect_satellite_signal(signal, threshold=0.5, peak_distance=100):
    """
    Detect satellite signals in a given signal.

    Args:
    - signal (array-like): The input signal.
    - threshold (float): Threshold for peak detection.
    - peak_distance (int): Minimum peak distance.

    Returns:
    - peaks (array-like): Indices of detected peaks.
    """
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)
    return peaks

def analyze_peaks(signal, peaks, sample_rate):
    """
    Analyze the detected peaks to determine frequency and strength.

    Args:
    - signal (array-like): The input signal.
    - peaks (array-like): Indices of detected peaks.
    - sample_rate (float): Sampling rate of the signal.

    Returns:
    - frequencies (array-like): Frequencies corresponding to the peaks.
    - strengths (array-like): Strengths of the detected signals.
    """
    spectrum = fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sample_rate)
    peak_frequencies = frequencies[peaks]
    peak_strengths = np.abs(spectrum[peaks])
    return peak_frequencies, peak_strengths

