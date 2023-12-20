import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import qi
import constants

# Connect to Pepper's NAOqi API
robot_ip = "your_pepper_ip"
port = 9559
session = ALProxy("ALBehaviorManager", robot_ip, port)

# Launch the behavior you created in Choregraphe
behavior_name = "MyBehavior"
session.startBehavior(behavior_name)

# You can also stop or control the behavior as needed
# session.stopBehavior(behavior_name)