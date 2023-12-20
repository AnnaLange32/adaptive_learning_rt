# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants
from robot_helpers import *
import robot_text
import numpy as np


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port


close_running_behavs()



# set speech rate
speech_rate_base = 89
speech_rate_swahili = 75
pitch_shift = 1.15

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + robot_ip + ":" + str(port))


# Get the ALMotion service
motion_service = session.service("ALMotion")
speech_service = session.service("ALTextToSpeech")
posture_service = session.service("ALRobotPosture")
behavior_mng_service = session.service("ALBehaviorManager")
memory_service = session.service("ALMemory")

## Get the ALAnimatedSpeech service
animated_speech = session.service("ALAnimatedSpeech") #says a text and animates it with movements
speak_move_service = session.service("ALSpeakingMovement")
speech_service.setParameter("speed", speech_rate_base)
speech_service.setParameter("pitchShift", pitch_shift)
lang = speech_service.getAvailableLanguages()
print "Available languages: " + str(lang)
#speech_service.setLanguage()

# Speak the text with animation
robot_speech(robot_text.robot_ex1)


# run through emotion assessment
joy, bored, frust = emotion_assessment()

time.sleep(1)

robot_speech(robot_text.robote_ex2)
posture_service.goToPosture("StandInit", 0.5)