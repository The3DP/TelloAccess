import cv2
import time
from djitellopy import Tello

# Initialize the Tello drone
tello = Tello()

def main():
    try:
        # Connect to the Tello drone
        tello.connect()

        # Print battery percentage
        print(f"Battery: {tello.get_battery()}%")

        # Start the video stream
        tello.streamon()

        # Wait for the drone to stabilize
        time.sleep(2)

        # Take off
        tello.takeoff()

        # Set the drone to fly up and stabilize
        tello.move_up(30)
        time.sleep(2)

        # Spin slowly to the left for 3 seconds
        tello.rotate_counter_clockwise(90)  # Spins counter-clockwise for 90 degrees (slowly)
        time.sleep(3)

        # Spin slowly to the right for 3 seconds
        tello.rotate_clockwise(90)  # Spins clockwise for 90 degrees (slowly)
        time.sleep(3)

        # Move forward 5 cm
        tello.move_forward(5)
        time.sleep(2)

        # Slowly land
        tello.land()

        # Stop the video stream
        tello.streamoff()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        tello.end()

if __name__ == "__main__":
    main()

# Start video capture
while True:
    frame = tello.get_frame_read().frame
    cv2.imshow("Live Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

































