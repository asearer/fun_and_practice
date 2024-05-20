# test_signal_processing.py
import unittest
import numpy as np
from detect_sat_signal_strength import detect_satellite_signal, analyze_peaks

class TestSignalProcessing(unittest.TestCase):
    
    def setUp(self):
        # Generate a synthetic satellite signal
        self.time = np.linspace(0, 10, 1000)
        self.sample_rate = 1 / (self.time[1] - self.time[0])
        self.signal = np.sin(2 * np.pi * 2 * self.time) + 0.5 * np.sin(2 * np.pi * 5 * self.time)
        
        # Add noise to the signal
        self.noise = np.random.normal(0, 0.2, self.signal.shape)
        self.noisy_signal = self.signal + self.noise

    def test_detect_satellite_signal(self):
        # Test peak detection
        detected_peaks = detect_satellite_signal(self.noisy_signal)
        self.assertIsInstance(detected_peaks, np.ndarray)
        self.assertGreater(len(detected_peaks), 0, "No peaks detected")

    def test_analyze_peaks(self):
        # Test analysis of detected peaks
        detected_peaks = detect_satellite_signal(self.noisy_signal)
        frequencies, strengths = analyze_peaks(self.noisy_signal, detected_peaks, self.sample_rate)
        
        self.assertIsInstance(frequencies, np.ndarray)
        self.assertIsInstance(strengths, np.ndarray)
        self.assertEqual(len(frequencies), len(detected_peaks), "Number of frequencies does not match number of peaks")
        self.assertEqual(len(strengths), len(detected_peaks), "Number of strengths does not match number of peaks")
        
        for freq in frequencies:
            self.assertGreaterEqual(abs(freq), 0, "Frequency is negative")

        for strength in strengths:
            self.assertGreaterEqual(strength, 0, "Strength is negative")

if __name__ == '__main__':
    unittest.main()

