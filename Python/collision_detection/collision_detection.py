import heapq

def detect_collisions(objects):
    # Priority queue to manage which object to process based on proximity (distance)
    priority_queue = [(obj['distance'], obj) for obj in objects]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        distance, obj = heapq.heappop(priority_queue)
        if distance < 10:  # Assume collision possible if within 10 meters
            print(f"Collision warning for {obj['name']} at {distance} meters!")
        if len(priority_queue) == 0:
            break

# Usage
objects = [
    {'name': 'Object1', 'distance': 5},
    {'name': 'Object2', 'distance': 15},
    {'name': 'Object3', 'distance': 7},
]
detect_collisions(objects)
