from djitellopy import Tello

# Create a Tello Object
drone = Tello()

# Connect to Tello Drone
drone.connect()

# Get battery status
print("Battery:", drone.get_battery())

# Take off
drone.takeoff()

# Fly up 5 seconds
drone.move_up(100)

# Fly down 2.5 seconds
drone.move_down(50)

# Fly forward 2.5 seconds
drone.move_forward(50)

# Rotate clockwise
drone.rotate_clockwise(90)

# Move forward
drone.move_forward(60)

# Rotate counter clockwise
drone.rotate_counter_clockwise(180)

# Move forward
drone.move_forward(60)

# Land
drone.land()

# Configuration
config = True
var = (118, 260, 559)

# Error handling
if "ERR" in var:  # Replace with meaningful condition
    # Drone is finished flying
    print("An error occurred while operating the drone.")
    print("Please check the drone's operation logs.")
