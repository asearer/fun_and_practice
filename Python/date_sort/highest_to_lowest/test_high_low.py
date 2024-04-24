import unittest
from high_low_date_sort import high_low_date_sort  

class TestHighLowDateSort(unittest.TestCase):

    def test_basic_sort(self):
        dates = ["2023 04 01", "2023 01 01", "2022 12 31"]
        expected = ["2023 04 01", "2023 01 01", "2022 12 31"]
        self.assertEqual(high_low_date_sort(dates), expected)

    def test_different_years(self):
        dates = ["2020 01 01", "2023 01 01", "2021 06 15"]
        expected = ["2023 01 01", "2021 06 15", "2020 01 01"]
        self.assertEqual(high_low_date_sort(dates), expected)

    def test_same_year_different_months(self):
        dates = ["2023 05 20", "2023 01 30", "2023 07 15"]
        expected = ["2023 07 15", "2023 05 20", "2023 01 30"]
        self.assertEqual(high_low_date_sort(dates), expected)

    def test_with_different_formats(self):
        dates = ["01-06-2023", "15-07-2022", "30-12-2023"]
        date_format = "%d-%m-%Y"
        expected = ["30-12-2023", "01-06-2023", "15-07-2022"]
        self.assertEqual(high_low_date_sort(dates, date_format), expected)

    def test_with_time_stamps(self):
        dates = ["2023-04-01 12:00", "2023-01-01 00:00", "2022-12-31 23:59"]
        date_format = "%Y-%m-%d %H:%M"
        expected = ["2023-04-01 12:00", "2023-01-01 00:00", "2022-12-31 23:59"]
        self.assertEqual(high_low_date_sort(dates, date_format), expected)

if __name__ == "__main__":
    unittest.main()
