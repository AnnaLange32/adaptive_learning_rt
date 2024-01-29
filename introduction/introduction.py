# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import qi
import constants
from robot_helpers import *
import robot_text


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port

close_running_behavs()

# Speech rate (adjust to change speed)

speech_rate = 89

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + robot_ip + ":" + str(port))


# Get the ALMotion service
motion_service = session.service("ALMotion")
speech_service = session.service("ALTextToSpeech")
posture_service = session.service("ALRobotPosture")
behavior_mng_service = session.service("ALBehaviorManager")

## Get the ALAnimatedSpeech service
animated_speech = session.service("ALAnimatedSpeech") #says a text and animates it with movements
speak_move_service = session.service("ALSpeakingMovement")
posture_service.goToPosture("StandInit", 0.5)
speech_service.setParameter("speed", speech_rate)


## Start active tracking

behavior_mng_service.runBehavior('p50_study1-5ba9db/basic_awareness_ON', _async=True)

# Speak the text with animation

robot_speech(robot_text.robot_intro)

## Start examples

# Speak the text with animation
time.sleep(1)
robot_speech(robot_text.robot_ex1)


# run through emotion assessment
joy, bored, frust = emotion_assessment()

time.sleep(1)

robot_speech(robot_text.robot_ex2)
posture_service.goToPosture("StandInit", 0.5)
close_running_behavs()
