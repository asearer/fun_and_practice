import unittest
import heapq

def detect_collisions(objects):
    priority_queue = [(obj['distance'], obj['name']) for obj in objects]
    heapq.heapify(priority_queue)
    results = []
    while priority_queue:
        distance, name = heapq.heappop(priority_queue)
        if distance < 10:
            results.append(f"Collision warning for {name} at {distance} meters!")
    return results

class TestDetectCollisions(unittest.TestCase):
    def test_collision_detection(self):
        objects = [{'name': 'Object1', 'distance': 5}, {'name': 'Object2', 'distance': 15}, {'name': 'Object3', 'distance': 7}]
        results = detect_collisions(objects)
        self.assertIn("Collision warning for Object1 at 5 meters!", results)
        self.assertIn("Collision warning for Object3 at 7 meters!", results)
        self.assertNotIn("Collision warning for Object2 at 15 meters!", results)

if __name__ == '__main__':
    unittest.main()
