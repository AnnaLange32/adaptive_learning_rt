# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants
import numpy as np
import pandas as pd
import robot_text

print('ok')
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


            emotion_scores = [1, 2, 3]
            emotion_scores[0] = joy
            emotion_scores[1] = bored
            emotion_scores[2] = frust

            # Load existing data
            try:
                existing_data = pd.read_csv('scores.csv', index_col=0)

                # If the file is empty, create an empty DataFrame
                if existing_data.empty:
                    existing_data = pd.DataFrame()
            except (IOError, pd.errors.EmptyDataError):
                # If the file doesn't exist or is empty, create an empty DataFrame
                existing_data = pd.DataFrame()

            # Create a dictionary with the new data
            new_data_dict = {
                'Enjoyment': [joy],
                'Boredom': [bored],
                'Frustration': [frust]
            }

            # Create a DataFrame with the new data
            new_data = pd.DataFrame(new_data_dict)

            # Concatenate the existing data with the new data
            all_data = pd.concat([existing_data, new_data])

            # Reset the index
            all_data = all_data.reset_index(drop=True)

            # Save the entire dataset
            all_data.to_csv('scores.csv', index_label='Iter')
            break
            # END OF EMOTION ASSESSMENT

    return joy, bored, frust

def retrieve_tag(tag_data):


    '''This should not be in robot helpers.'''
    object_ID = tag_data.get("object")
    location_ID = tag_data.get('location')

    object_current = constants.tag_to_object_mapping.get(object_ID, None)
    location_current = constants.tag_to_location_mapping.get(location_ID, None)
    object_location = object_current + ' ' + location_current
    if object_current == 'Jam':
        location_correct = location_ID

    else:
        location_correct = 'None'
    return object_current,location_current, location_correct, object_location



def retrieve_obj_and_location(tag_data):

    '''This function is for the simulation only.'''

    object_current = tag_data.get("object")
    location_index = int(tag_data.get('location'))

    location_current = constants.positions_cur_sw[int(location_index)]
    object_location = object_current + ' ' + location_current

    location_correct = object_current + ' ' + constants.positions_cur_sw[constants.objects_sw.index(object_current)]


    return object_current,location_current, location_correct, object_location


def close_running_behavs():

    behavior_mng_service = session.service("ALBehaviorManager")
    names = behavior_mng_service.getRunningBehaviors()

    print(names)

    for behavior in names:
        behavior_mng_service.stopBehavior(behavior)

    print(names)


def robot_speech(section):

    '''This function executes Pepper speech and behavior. The input needs to be in the following format:

    section = [
    [time11, text1, behav1, time12],
    ...
    [time51, text5, behav5, time52],
    etc.
    ]

    where text is a string of words for Pepper to say, the behavior is a special behavior to execute during the speech
    and time can be used to ensure the timing of speech to behavior is good.
    The speech is executed as an animated speech.
    The defined text can include the behavior mode ^mode(), pitch \\vct=120\\ and rate \\rspd=80\\ info.
    '''


    for line in section:



        behavior_mng_service.runBehavior(line[2], _async=True)

        time.sleep(line[0])  # extracts the first time

        animated_speech.say(line[1])



        time.sleep(line[3]) # extracts the second time




def robot_speech2(section, word_o = '', word_p = '', word_l = ''):

    '''This function executes Pepper speech and behavior. The input needs to be in the following format:

    section = [
    [time11, text11, text12, time12],
    ...
    [time51, text51, text52, time52],
    etc.
    ]

    where text is a string of words for Pepper to say.
    The speech is executed as an animated speech.
    The defined text can include the behavior mode ^mode(), pitch \\vct=120\\ and rate \\rspd=80\\ info.
    '''


    for line in section:

        print(line)

        time.sleep(line[0])  # extracts the first time

        animated_speech.say(line[1])

        time.sleep(line[3]) # extracts the second time

        if line[2] != (''):
            animated_speech.say(word_o)
            animated_speech.say(word_p)
            animated_speech.say(word_l)

        animated_speech.say(line[2])
