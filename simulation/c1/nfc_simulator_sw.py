
# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import qi
from robot_helpers import *
from twisted.internet import reactor
import random
import numpy as np


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port

def detect_simulated_nfc_tags():

    # generate a random number between 0 and 1
    random_number = random.random()

    # get the lists of defined objects and locations
    object_list = constants.objects_sw
    location_list = constants.reader_nr


    # SIMULATION: Set the rate at which correct decisions are made
    treshold = 0.5

    # SIMULATION: Simulate NFC tag detection

    if random_number < treshold:

        # SIMULATION: Simulate a correct choice

        object = random.choice(object_list)
        location = object_list.index(object)
        tag_data = {'object': object, 'location': location}
        print("NFC Tag detected is a correct placement:", tag_data)
        tag_time = time.time()


    else:
        #  SIMULATION: Simulate an incorrect (random) choice
        tag_data = {'object': random.choice(object_list), 'location': random.choice(location_list)}
        print("NFC Tag detected is an incorrect placement:", tag_data)
        tag_time = time.time()

    # Call the function to process the detected tag data
    process_detected_tags(tag_data, tag_time)

    # Simulation: Schedule the next detection after a 5-second or a 15-second interval

    next_tag = random.randint(5,5)
    reactor.callLater(next_tag, detect_simulated_nfc_tags)



def process_detected_tags(tag_data, tag_time):


    # Define the interval (in seconds) for the emotion assessment (5 minutes in the experiment case)
    interval1 = 3 * 60  # 5 minutes * 60 seconds/minutes for emotion assessment
    interval2 = 5 # for additional hint

    placement_time = random.randint(0, 10) #for simulation purposes, simulate no placements for some time
    time.sleep(placement_time)
    current_time = time.time()

    if current_time - tag_time >= interval2:
        text_to_say1 = ("Weiter geht's!")
        text_to_say2 = ("Ich kann dir nur Rueckmeldung geben, wenn du eine Platzierung vornimmst.")

        # Execute robot speech and actions
        behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 10', _async=True)
        time.sleep(2)
        animated_speech.say(text_to_say1)
        time.sleep(1)
        animated_speech.say(text_to_say2)

    # Check if it's time to perform the emotion assessment

    if current_time - experiment_start_time >= interval1:


        # Update the start time for the next interval
        global experiment_start_time
        experiment_start_time = current_time

        # run through emotion assessment
        behavior_mng_service.runBehavior('p50_study1-5ba9db/assessment all emotions', _async=True)

        animated_speech.say('Koenntest du deine Gefuehle auf meinem Bildschirm eingeben?')

        emotion_assessment()

        time.sleep(3)
        animated_speech.say('Danke weiter geht es.')
        # END OF EMOTION ASSESSMENT

    # retrieve object and location from tag

    object_current, location_current, location_correct, object_location = retrieve_obj_and_location(tag_data)


    # define robot speech for initial object picked

    text_to_say1 = ('Das ist: ')
    speech_service.setParameter("speed", speech_rate_swahili)
    text_to_say2 = (object_current)
    speech_service.setParameter("speed", speech_rate_base)
    time.sleep(2)
    text_to_say3 = ('Bitte platziere das Objekt an der folgenden Stelle: ')
    speech_service.setParameter("speed", speech_rate_swahili)
    text_to_say4 = (location_correct)
    speech_service.setParameter("speed", speech_rate_base)


    # Execute robot speech and actions
    behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 8', _async=True)
    time.sleep(3)
    animated_speech.say(text_to_say1)
    time.sleep(1)
    animated_speech.say(text_to_say2)
    time.sleep(2)
    animated_speech.say(text_to_say3)
    time.sleep(2)
    animated_speech.say(text_to_say4)

    # update  occurence memory :
    constants.memory_occurence[object_current] += 1
    # update associated memory :
    constants.memory_association[object_current] += 1
    # update occurence memory :
    for word in location_correct:
        if word in constants.memory_occurence:
            # Increment word count for each word in memory
            constants.memory_occurence[word] += 1
    # update associated memory :
    constants.memory_association[object_current] += 1



# decide if location CORRECT or INCORRECT

    if object_location == location_correct:
        perf_score = 1
        np.append(constants.memory_performance, perf_score)
        print('THIS IS A CORRECT LOCATION!', object_location, location_correct)
        # define the robot speech
        text_to_say1 = ("^mode(cotextual) Diese Platzierung ist: ")
        speech_service.setParameter("speed", speech_rate_swahili)
        time.sleep(2)
        text_to_say2 = (object_location)
        speech_service.setParameter("speed", speech_rate_base)
        time.sleep(2)
        text_to_say3 = ("^mode(cotextual) Super! Das ist korrekt!")
        text_to_say4 = ("Du kannst nun mit einem anderen Objekt weitermachen.")

        # execute the robot speech and action
        time.sleep(3)
        animated_speech.say(text_to_say1)
        time.sleep(1)
        animated_speech.say(text_to_say2)
        behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 9', _async=True)
        time.sleep(5)
        animated_speech.say(text_to_say3)
        time.sleep(1)
        animated_speech.say(text_to_say4)
        time.sleep(1)

        # updated occurence memory
        for word in object_location:
            if word in constants.memory_occurence:
                # Increment word count for each word in memory
                constants.memory_occurence[word] += 1
        # update associated memory
        for word in object_location:
            if word in constants.memory_occurence:
                # Increment word count for each word in memory
                constants.memory_association[word] += 1

    else:
        perf_score = -1
        np.append(constants.memory_performance, perf_score)
        # define the robot speech

        text_to_say1 = ("^mode(cotextual) Diese Platzierung ist: ")  # behavior 4
        speech_service.setParameter("speed", speech_rate_swahili)
        time.sleep(2)
        text_to_say2 = (object_location)
        speech_service.setParameter("speed", speech_rate_base)
        time.sleep(2)
        text_to_say3 = ("^mode(cotextual) Aber das ist falsch.")
        text_to_say4 = ("Die korrekte Platzierung lautet:")
        speech_service.setParameter("speed", speech_rate_swahili)
        time.sleep(2)
        text_to_say5 = (location_correct)
        speech_service.setParameter("speed", speech_rate_base)


        # execute the robot speech and action
        time.sleep(3)
        animated_speech.say(text_to_say1)
        time.sleep(1)
        animated_speech.say(text_to_say2)

        time.sleep(1)
        animated_speech.say(text_to_say3)
        time.sleep(1)
        animated_speech.say(text_to_say4)
        time.sleep(1)
        animated_speech.say(text_to_say5)
        time.sleep(1)

        # update occurence memory
        for word in object_location:
            if word in constants.memory_occurence:
                # Increment word count for each word in memory
                constants.memory_occurence[word] += 1
        # update associated memory
        for word in object_location:
            if word in constants.memory_occurence:
                # Increment word count for each word in memory
                constants.memory_association[word] += 1


        # update occurence memory
        for word in location_correct:
            if word in constants.memory_occurence:
                # Increment word count for each word in memory
                constants.memory_occurence[word] += 1
        # update associated memory
        constants.memory_association[object_current] += 1

    # save outputs STILL NEED TO FIGURE OUT BEST WAY TO SAVE THESE AT FINAL STAGE

    print(constants.memory_occurence)

    print(constants.memory_association)

    print(constants.memory_performance)



if __name__ == "__main__":

    # set speech rate

    speech_rate_base = 85
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
    tablet_service = session.service("ALTabletService")


    ## Get the ALAnimatedSpeech service
    animated_speech = session.service("ALAnimatedSpeech")  # says a text and animates it with movements
    speak_move_service = session.service("ALSpeakingMovement")

    # close running behaviors
    close_running_behavs()


    # Start the tag detection
    experiment_start_time = time.time()
    experiment_end_time = experiment_start_time + 30 * 60  # 30 minutes * 60 seconds/minute

    reactor.callLater(0, detect_simulated_nfc_tags)

    # Start the reactor to run the Twisted event loop
    posture_service.goToPosture("StandInit", 0.5)
    reactor.run()

