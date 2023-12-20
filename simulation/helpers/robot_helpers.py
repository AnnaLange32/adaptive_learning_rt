# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants
import numpy as np



# Connect to the robot
session = qi.Session()
session.connect("tcp://" + constants.ip + ":" + str(constants.port))


# Get the ALMotion service
motion_service = session.service("ALMotion")
speech_service = session.service("ALTextToSpeech")
posture_service = session.service("ALRobotPosture")
behavior_mng_service = session.service("ALBehaviorManager")
memory_service = session.service("ALMemory")
tablet_service = session.service("ALTabletService")

## Get the ALAnimatedSpeech service
animated_speech = session.service("ALAnimatedSpeech")  # says a text and animates it with movements
speak_move_service = session.service("ALSpeakingMovement")


def emotion_assessment():

    ''''''


    while True:

       # get the currently running behaviors and check if the emotion assesment is completed
        running_behaviors = behavior_mng_service.getRunningBehaviors()
        if "p50_study1-5ba9db/assessment all emotions" not in running_behaviors:
            # The first behavior has completed, start the second behavior

            tablet_service.hideImage()
            posture_service.goToPosture("StandInit", 0.5)
            bored = memory_service.getData('P50_study1/variables/bored')

            frust = memory_service.getData("P50_study1/variables/frust")

            joy = memory_service.getData("P50_study1/variables/joy")

            joy = int(joy)
            bored = int(bored)
            frust = int(frust)
            print('The joy score was: ', joy, ', the bored score was: ', bored, ', the frustration score was: ', frust)

            emotion_names = ['Enjoyment', 'Boredom', 'Frustration']
            emotion_scores = [1, 2, 3]
            emotion_scores[0] = joy
            emotion_scores[1] = bored
            emotion_scores[2] = frust

            # Save emotion_names and emotion_scores to 'scores.csv'
            np.savetxt('scores.csv', np.column_stack((emotion_names, emotion_scores)), delimiter=',', fmt='%s')
            break
            # END OF EMOTION ASSESSMENT

def retrieve_obj_and_location(tag_data):

    object_ID = tag_data.get("object")
    location_ID = tag_data.get('location')
    print('The current location ID is: ', location_ID)
    print('The current object ID is: ', object_ID)

    location_current = constants.positions_cur_sw[int(location_index)]
    object_location = object_current + ' ' + location_current
    print('The object is currently in:', object_location)
    location_correct = object_current + ' ' + constants.positions_cur_sw[constants.objects_sw.index(object_current)]
    print('The object should be in: ', location_correct)

    return object_current,location_current, location_correct, object_location



def retrieve_obj_and_location(tag_data):

    '''This function is for the simulation only.'''

    object_current = tag_data.get("object")
    location_index = int(tag_data.get('location'))
    print('The current location is: ', location_index)
    print('The current object is: ', object_current)
    location_current = constants.positions_cur_sw[int(location_index)]
    object_location = object_current + ' ' + location_current
    print('The object is currently in:', object_location)
    location_correct = object_current + ' ' + constants.positions_cur_sw[constants.objects_sw.index(object_current)]
    print('The object should be in: ', location_correct)

    return object_current,location_current, location_correct, object_location


def close_running_behavs():

    behavior_mng_service = session.service("ALBehaviorManager")
    names = behavior_mng_service.getRunningBehaviors()

    print(names)

    for behavior in names:
        behavior_mng_service.stopBehavior(behavior)

    print(names)


