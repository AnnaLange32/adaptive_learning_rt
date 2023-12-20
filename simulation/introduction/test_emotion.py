# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import time
import qi
import constants
import numpy as np


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port
# set speech rate
speech_rate_base = 79
speech_rate_swahili = 70

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
posture_service.goToPosture("StandInit", 0.5)
speech_service.setParameter("speed", speech_rate_base)

# spoken text

text_to_say17 = ("^mode(contextual) Left means not, at all and right means very strong feeling. We can do a trial run now!")
text_to_say18 = ("Great, thank you! Then we'll get started now! Pick your first item and let's go!")


# run through emotion assessment



time.sleep(1)
# behavior_mng_service.stopBehavior('p50_study1-5ba9db/assessment all emotions', _async=True)
behavior_mng_service.runBehavior('p50_study1-5ba9db/assessment all emotions', _async=True)
animated_speech.say(text_to_say17)



# Set the initial time
experiment_start_time = time.time()
emotion_timer = time.time()
print(emotion_timer)
# Define the interval (in seconds) for the task (5 minutes in this case)
experiment_end_time =experiment_start_time + 2*60 # 30 minutes * 60 seconds/minute

while emotion_timer < experiment_end_time:

    current_time = time.time()
    running_behaviors = behavior_mng_service.getRunningBehaviors()


    if "p50_study1-5ba9db/assessment all emotions" not in running_behaviors:
        # The first behavior has completed, start the second behavior
        tabletService = session.service("ALTabletService")
        tabletService.hideImage()

        animated_speech.say(text_to_say18)
        bored = memory_service.getData('P50_study1/variables/bored')

        frust = memory_service.getData("P50_study1/variables/frust")

        joy = memory_service.getData("P50_study1/variables/joy")

        joy = int(joy)
        bored = int(bored)
        frust = int(bored)
        print('The joy score was: ', joy, ', the bored score was: ', bored, ', the frustration score was: ', frust)

        emotion_names = ['Enjoyment', 'Boredom', 'Frustration']
        emotion_scores = [1, 2, 3]
        emotion_scores[0] = joy
        emotion_scores[1] = bored
        emotion_scores[2] = frust

        # Save emotion_names and emotion_scores to 'scores.csv'
        np.savetxt('scores.csv', np.column_stack((emotion_names, emotion_scores)), delimiter=',', fmt='%s')
        break



    emotion_timer = current_time


animated_speech.say(text_to_say18)



