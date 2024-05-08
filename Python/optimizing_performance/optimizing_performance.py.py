import time

def complex_collision_detection():
    time.sleep(0.01)  # Simulate complex calculations
    return True

def simple_collision_detection():
    time.sleep(0.001)  # Simulate simpler calculations
    return False

frame_time_target = 0.016  # 60 FPS

start_time = time.time()
if complex_collision_detection():
    print("Complex collision detected.")
end_time = time.time()

if (end_time - start_time) > frame_time_target:
    print("Switching to simpler detection due to performance constraints.")
    simple_collision_detection()
