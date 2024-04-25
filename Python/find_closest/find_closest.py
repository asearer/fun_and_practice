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

def find_closest_people(data, target, key, n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    # Calculate absolute differences and sort by them, adding name as a secondary sort key for consistency
    data_sorted = sorted(data, key=lambda x: (abs(x[key] - target), x['name']))
    return data_sorted[:n]

# Example usage:
closest_people = find_closest_people(people, target_age, 'age', 3)
print(closest_people)


