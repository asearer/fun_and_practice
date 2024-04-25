import unittest

# Define the dataset and target
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 40},
    {'name': 'Eve', 'age': 28},
    {'name': 'Frank', 'age': 33},
    {'name': 'Grace', 'age': 45}
]
target_age = 29

# Function to find the top N closest items
def find_closest_people(data, target, key, n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    # Calculate absolute differences and sort by them, adding name as a secondary sort key for consistency
    data_sorted = sorted(data, key=lambda x: (abs(x[key] - target), x['name']))
    return data_sorted[:n]

class TestFindClosestPeople(unittest.TestCase):

    def test_basic_functionality(self):
        expected = [{'name': 'Bob', 'age': 30}, {'name': 'Eve', 'age': 28}, {'name': 'Alice', 'age': 25}]
        result = find_closest_people(people, target_age, 'age', 3)
        self.assertEqual(result, expected)

    def test_request_more_people_than_available(self):
        result = find_closest_people(people, target_age, 'age', 10)
        self.assertEqual(len(result), 7)  # Should return all available entries

    def test_negative_n(self):
        result = find_closest_people(people, target_age, 'age', -1)
        self.assertEqual(result, [])  # Expecting an empty list

    def test_zero_n(self):
        result = find_closest_people(people, target_age, 'age', 0)
        self.assertEqual(result, [])  # Expecting an empty list

    def test_non_integer_ages(self):
        modified_people = [{'name': 'Alice', 'age': 'twenty-five'}, {'name': 'Bob', 'age': 30}]
        with self.assertRaises(TypeError):
            find_closest_people(modified_people, target_age, 'age', 1)

    def test_empty_dataset(self):
        result = find_closest_people([], target_age, 'age', 3)
        self.assertEqual(result, [])

    def test_non_existent_key(self):
        with self.assertRaises(KeyError):
            find_closest_people(people, target_age, 'height', 3)

if __name__ == '__main__':
    unittest.main()


