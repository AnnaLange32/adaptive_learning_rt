
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
import qi
import constants


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port
# Text to be spoken
text_to_say = "Hello!  Take some time to speak and then resume movement and then continue to speak for somemore time? Now I will make a special move ^start(animations/Stand/Gestures/You_1)"
#text_to_say = "Hello. Look, I can stop moving, and after I can resume moving, you see. Take some time to speak and then resume movement and then continue to speak for somemore time?" #^mode(contextual) ^mode(disabled)

# Speech rate (adjust to change speed)

speech_rate = 80

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + robot_ip + ":" + str(port))

# Get the ALMotion service
motion_service = session.service("ALMotion")
speech_service = session.service("ALTextToSpeech")
posture_service = session.service("ALRobotPosture")





## Get the ALAnimatedSpeech service
animated_speech = session.service("ALAnimatedSpeech") #says a text and animates it with movements
speech_service.setParameter("speed", speech_rate)
# Speak the text with animation
animated_speech.say(text_to_say)
# Send robot to Stand Zero
posture_service.goToPosture("StandInit", 0.5)

# Trigger the "Hey_6" animation
#animated_speech.setBodyLanguageMode(1)  # Enable body language
#animated_speech.setStimulus(["Hey_6"])  # Trigger the "Hey_6" animation

# Wait for the animation to complete
#animated_speech.waitUntilDone()

# Disable body language
#animated_speech.setBodyLanguageMode(0)
