import heapq

def detect_collisions(objects):
    """
    Detect and report objects that are within a collision range of 10 meters.
    
    This function processes a list of objects, each represented as a dictionary
    containing 'name' and 'distance' keys. It uses a priority queue to process objects
    based on their proximity. A collision warning is issued for objects closer than 10 meters.

    Parameters:
    objects (list of dict): A list of dictionaries where each dictionary contains
                            'name' (str) and 'distance' (float) keys representing the name and the
                            distance of the object from a reference point respectively.

    Returns:
    None: Outputs to the console directly.

    Example:
    >>> detect_collisions([{'name': 'Object1', 'distance': 5},
                           {'name': 'Object2', 'distance': 15},
                           {'name': 'Object3', 'distance': 7}])
    Collision warning for Object1 at 5 meters!
    Collision warning for Object3 at 7 meters!
    """
    # Create a priority queue with all objects, sorted by their distance
    priority_queue = [(obj['distance'], obj) for obj in objects]
    heapq.heapify(priority_queue)
    
    # Process the queue until it is empty
    while priority_queue:
        # Pop the object with the smallest distance
        distance, obj = heapq.heappop(priority_queue)
        
        # Check if the object's distance is within the collision range
        if distance < 10:
            print(f"Collision warning for {obj['name']} at {distance} meters!")
        
        # Early exit condition: redundant due to the while loop condition
        if len(priority_queue) == 0:
            break

# Usage example
objects = [
    {'name': 'Object1', 'distance': 5},
    {'name': 'Object2', 'distance': 15},
    {'name': 'Object3', 'distance': 7},
]
detect_collisions(objects)

