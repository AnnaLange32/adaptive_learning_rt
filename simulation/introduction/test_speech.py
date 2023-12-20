# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants
from robot_helpers import *
import numpy as np



# set speech rate
speech_rate_base = 83
speech_rate_swahili = 70
pitch_shift = 1.15

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + constants.ip + ":" + str(constants.port))



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
#speech_service.setLangu
#
#
#text_to_say18 = (" \\vct=130\\ Super, \\vct=110\\ dann fangen wir jetzt an! Such dir einen ersten Gegenstand aus und. \\vct=130\\  los  \\vct=140\\  geht \\vct=150\\ es!")
animated_speech.say("mmmmmbaehlea?")



#for object in constants.objects_sw:
    #animated_speech.say(object)

    #time.sleep(4.5)
    #animated_speech.say(object)
    #time.sleep(1.5)


#for prepoposition in constants.prepositions_sw:

    #animated_speech.say(prepoposition)
    #time.sleep(4.5)
    #animated_speech.say(prepoposition)
    #time.sleep(1.5)


#for position in constants.locations_sw:
    #animated_speech.say(position)
    #time.sleep(4.5)
    #animated_speech.say(position)
    #time.sleep(1.5)


