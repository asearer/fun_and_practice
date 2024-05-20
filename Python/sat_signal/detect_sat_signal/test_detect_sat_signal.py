import unittest
import numpy as np
from scipy.signal import find_peaks

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
    
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)
    
    return peaks

class TestDetectSatelliteSignal(unittest.TestCase):

    def test_no_signal(self):
        """Test detection with no signal (all zeros)."""
        signal = np.zeros(1000)
        peaks = detect_satellite_signal(signal)
        self.assertEqual(len(peaks), 0)

    def test_single_peak(self):
        """Test detection with a single peak."""
        signal = np.zeros(1000)
        signal[500] = 1  # single peak
        peaks = detect_satellite_signal(signal, threshold=0.5)
        self.assertEqual(len(peaks), 1)
        self.assertEqual(peaks[0], 500)

    def test_multiple_peaks(self):
        """Test detection with multiple peaks."""
        signal = np.zeros(1000)
        signal[100] = 1
        signal[300] = 1
        signal[500] = 1
        signal[700] = 1
        signal[900] = 1
        peaks = detect_satellite_signal(signal, threshold=0.5, peak_distance=100)
        self.assertEqual(len(peaks), 5)
        np.testing.assert_array_equal(peaks, [100, 300, 500, 700, 900])

    def test_noise(self):
        """Test detection with noisy signal."""
        time = np.linspace(0, 10, 1000)
        signal = np.sin(2 * np.pi * 2 * time) + 0.5 * np.sin(2 * np.pi * 5 * time)
        noise = np.random.normal(0, 0.2, signal.shape)
        noisy_signal = signal + noise
        peaks = detect_satellite_signal(noisy_signal, threshold=0.5, peak_distance=50)
        # We cannot predict the exact peaks due to noise, but we can check if we get some peaks.
        self.assertTrue(len(peaks) > 0)

    def test_custom_threshold(self):
        """Test detection with a custom threshold."""
        signal = np.zeros(1000)
        signal[100] = 0.4
        signal[300] = 0.6
        peaks = detect_satellite_signal(signal, threshold=0.5)
        self.assertEqual(len(peaks), 1)
        self.assertEqual(peaks[0], 300)

    def test_custom_peak_distance(self):
        """Test detection with a custom peak distance."""
        signal = np.zeros(1000)
        signal[100] = 1
        signal[150] = 1
        peaks = detect_satellite_signal(signal, threshold=0.5, peak_distance=10)
        self.assertEqual(len(peaks), 2)
        np.testing.assert_array_equal(peaks, [100, 150])

if __name__ == '__main__':
    unittest.main()
