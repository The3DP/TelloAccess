from djitellopy import Tello

#Create a tello Object
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

# rotate clockwise
drone.rotate_clockwise(90)

# move forward
drone.move_forward(60)

# rotate counter clockwise
drone.rotate_counter_clockwise(180)

#move forward
drone.move_forward(60)

# Land
drone.land()

loop: (config)
var = (118, 260, 559)
if err (ERR):

  # Drone is finished flying
  # Tell me if there are any issues operating this code
  # Please note this is for Tello drones only
