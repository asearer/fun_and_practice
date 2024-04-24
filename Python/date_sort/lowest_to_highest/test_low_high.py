import unittest
from low_high_date import low_high_date_sort  

class TestLowHighDateSort(unittest.TestCase):

    def test_sorts_dates_in_ascending_order(self):
        dates = ["2023 04 01", "2023 01 01", "2022 12 31"]
        expected = ["2022 12 31", "2023 01 01", "2023 04 01"]
        self.assertEqual(low_high_date_sort(dates), expected)

    def test_handles_different_date_formats(self):
        dates = ["01-06-2023", "15-07-2022", "30-12-2023"]
        date_format = "%d-%m-%Y"
        expected = ["15-07-2022", "01-06-2023", "30-12-2023"]
        self.assertEqual(low_high_date_sort(dates, date_format), expected)

if __name__ == "__main__":
    unittest.main()
