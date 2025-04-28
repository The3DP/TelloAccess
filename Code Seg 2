import socket
import time

# Tello IP and port
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
LOCAL_PORT = 9000

# Initialize a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', LOCAL_PORT))

def send_command(command):
    try:
        sock.sendto(command.encode('utf-8'), (TELLO_IP, TELLO_PORT))
        print(f"Sent command: {command}")

        # Receive response from Tello
        response, _ = sock.recvfrom(1024)
        print(f"Response: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Error sending command: {e}")

# Put Tello in SDK mode
send_command("command")

# Take off to make the drone active
send_command("takeoff")
time.sleep(5)

# Example of requesting bottom camera data (positioning sensor data)
send_command("downvision 1")  # SDK may provide raw data for position and stability

# Hover for a few seconds
time.sleep(5)

# Land after testing
send_command("land")

# Close the socket after finishing
sock.close()
# Drone is finished flying
# Tell me if there are any issues operating this code
# Please note this is for Tello drones only
