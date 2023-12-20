import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
import qi
import constants


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + robot_ip + ":" + str(port))

# Get the ALBackgroundMovement service
background_movement = session.service("ALBackgroundMovement")

# Disable the BACKGROUND_MOVEMENT AutonomousAbility
background_movement.setEnabled(False)