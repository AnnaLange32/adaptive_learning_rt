# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants
from robot_helpers import *
import numpy as np


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port


close_running_behavs()

# Text to be spoken
text_to_say1 = ("^mode(cotextual) \\emph=2\\ Das, zum Beispiel ist eine Flasche. Auf Swahili: chupa.") # behavior 4
text_to_say2 = ("^mode(contextual) Wenn du jetzt im Spiel die Flasche anheben wuerdest,  ^mode(disabled) wuerde ich dir sagen")
text_to_say3 = ('\\readmode=word\\ chupa, kwenye, rafu')
text_to_say4 = ("was so viel bedeutet wie 'Flasche, auf, Regal'.")
text_to_say5= ("^mode(contextual) Also muesstest du die Flasche auf die weisse Box dort auf dem Regal stellen.")  # behavior 5
text_to_say6 = ("^mode(contextual) Um die Bedeutung herauszufinden, musst du aber natuerlich erstmal verschiedene Positionen ausprobieren.")
text_to_say7 = ("^mode(contextual) Wenn du die Flasche an eine falsche Position stellst, zum Beispiel hier unter den Tisch") # behavior 6
text_to_say8 = ("^mode(disabld)  sage ich dir auch, wo die Flasche gerade steht. ^mode(contextual) Also, um bei dem Beispiel zu bleiben wuerde ich sagen:")
text_to_say9 = ('^mode(disabled) \\readmode=word\\ chupa, chini ja, meza.') # original swahili: chini ya
text_to_say10 = ("aber das ist falsch.")
text_to_say11 = ("^mode(disabled) Nach einer falschen Plazierung, kannst du natuerlich weiter ausprobieren. ^mode(contextual) Bitte bewege immer nur einen Gegenstand nach dem anderen.")
text_to_say12 = ("^mode(contextual) Vieles wird sich auch im Laufe des Spieles ergeben, also fangen wir vielleicht einfach an. ")
text_to_say13 = ("^mode(random)   Ich freu mich drauf, mit dir zu spielen, du auch?") # behavior 3
text_to_say14 = ("^mode(disabled) Ich hoffe, du wirst Spass an dem Spiel haben!")
text_to_say15 = ("^mode(contextual)  In regelmaessigen Zeitabstaenden ^mode(disabled) werde ich dich waehrend des Spiels fragen, ^mode(contextual) wie stark du bestimmte Gefuehle  ^mode(disabled) im Moment empfindest.")
text_to_say16 = ("^mode(contextual)  Druecke dafuer einfach die am besten passende Antwort auf diesem Bildschirm auf meiner Brust.") # behavior 7
text_to_say17 = ("^mode(contextual)  Links bedeutet ueberhaupt nicht und rechts bedeutet sehr stark. Lass es uns direkt mal ausprobieren!")
text_to_say18 = (" \\vct=130\\ Super, \\vct=110\\ dann fangen wir jetzt an! Such dir einen ersten Gegenstand aus und. \\vct=130\\  los  \\vct=140\\  geht \\vct=150\\ es!")


# set speech rate
speech_rate_base = 83
speech_rate_swahili = 70
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
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 4', _async=True)
time.sleep(3)
animated_speech.say(text_to_say1)
time.sleep(1)
animated_speech.say(text_to_say2)
time.sleep(1)
speech_service.setParameter("speed", speech_rate_swahili)
animated_speech.say(text_to_say3)
speech_service.setParameter("speed", speech_rate_base)
time.sleep(1)
animated_speech.say(text_to_say4)
time.sleep(2)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 5', _async=True)
time.sleep(0.2)
animated_speech.say(text_to_say5)
time.sleep(1)
animated_speech.say(text_to_say6)
time.sleep(0.5)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 6', _async=True)
time.sleep(0.5)
animated_speech.say(text_to_say7)
time.sleep(2)
animated_speech.say(text_to_say8)
time.sleep(2)
speech_service.setParameter("speed", speech_rate_swahili)
animated_speech.say(text_to_say9)
speech_service.setParameter("speed", speech_rate_base)
time.sleep(2)
animated_speech.say(text_to_say10)
time.sleep(2)
animated_speech.say(text_to_say11)
time.sleep(2)
animated_speech.say(text_to_say12)
time.sleep(2)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 3', _async=True)
time.sleep(0.2)
animated_speech.say(text_to_say13)
time.sleep(2)
animated_speech.say(text_to_say14)
time.sleep(2)
animated_speech.say(text_to_say15)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 7', _async=True)
time.sleep(0.5)
animated_speech.say(text_to_say16)
time.sleep(1)
# execute emotion assessment behavior

behavior_mng_service.runBehavior('p50_study1-5ba9db/assessment all emotions', _async=True)

animated_speech.say(text_to_say17)


# run through emotion assessment
emotion_assessment()

time.sleep(1)

animated_speech.say(text_to_say18)
posture_service.goToPosture("StandInit", 0.5)