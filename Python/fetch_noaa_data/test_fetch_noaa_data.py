import unittest
from unittest.mock import patch, Mock
import pandas as pd
import requests  # Explicitly import requests
from fetch_noaa_data import fetch_noaa_data  # Ensure this import matches the actual file and function names

class TestFetchNOAAData(unittest.TestCase):

    def setUp(self):
        self.example_data = [{
            "time_tag": "2024-05-08T00:00:00Z",
            "kp_index": 5,
            "kp_station_count": 13
        }]

    @patch('requests.get')
    def test_successful_api_call(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = self.example_data
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Call the function
        result = fetch_noaa_data()

        # Check the result
        self.assertIsInstance(result, pd.DataFrame)
        self.assertFalse(result.empty)
        self.assertEqual(result.iloc[0]['kp_index'], 5)

    @patch('requests.get')
    def test_api_returns_empty_data(self, mock_get):
        # Mock an empty API response
        mock_response = Mock()
        mock_response.json.return_value = []
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Call the function
        result = fetch_noaa_data()

        # Check the result
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

    @patch('requests.get')
    def test_api_call_failure(self, mock_get):
        # Simulate an API failure
        mock_get.side_effect = requests.exceptions.RequestException("API failure")

        # Call the function
        result = fetch_noaa_data()

        # Check the result
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

    @patch('requests.get')
    def test_invalid_json_response(self, mock_get):
        # Mock an invalid JSON response
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        # Call the function
        result = fetch_noaa_data()

        # Check the result
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

if __name__ == '__main__':
    unittest.main()
