# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import random
import qi
from robot_helpers import *
import numpy as np
import serial
import time
import constants
import threading
import robot_text
import json
from multiprocessing.pool import ThreadPool



'''This code need a connection to Pepper robot. Currently the below code works with three readers. Can be used for conditions 1 to 3 (uncomment or comment which you need)
'''


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port


def read_port(args):
    # define the global variables
    global object_current
    global object_correct
    global location_current
    global location_correct
    global tag_time
    global readers_correct
    global reader_current
    global prev_loc_check

    port_name, port = args
    port.write(b'g')
    data = port.readline()
    tag, reader = extract_identifiers(data)
    print(tag, reader)

    if tag is not None and tag != '' and not np.isin(reader, readers_correct):
        tag_dict = {'object': tag, 'location': reader}
        print(tag, reader)
        reader_current = reader

        if reader == 'reader0':

            with lock:
                object_correct, location_start, location_correct = retrieve_tag(
                    tag_dict)
                tag_time = time.time()
        else:
            with lock:
                object_current, location_current, location_correct = retrieve_tag(tag_dict)
                tag_time = time.time()

            if not object_correct == object_current:
                object_current = ''
                location_current = ''
                location_correct = ''
                speech_service.setParameter("speed", speech_rate_base)
                animated_speech.say(
                    'Bitte stelle ein neues Objekt immer zuerst auf die Start Box, damit ich dir sagen kann wo es hingehoert.')


def detect_nfc_tags_parallel():
    # Use ThreadPool to parallelize port reading
    pool = ThreadPool(len(reader_ports))
    pool.map(read_port, reader_ports.items())
    pool.close()
    pool.join()


def detect_nfc_tags():
    '''This functions sends a request to the Arduiono RFID module.
     However I need to check if the port and reader order is consistent or if I need to work with a different identifier.'''

    # define the global variables
    global object_current
    global object_correct
    global location_current
    global location_correct
    global tag_time
    global readers_correct
    global reader_current

    # event.wait()

    for port_name, port in reader_ports.items():
        # print(port)

        port.write(b'g')
        data = port.readline()
        tag, reader = extract_identifiers(data)
        print(tag, reader)
        # print "Data from {}: {}".format(port_name, data)

        if tag is not None and tag != '' and not np.isin(reader, readers_correct):
            tag_dict = {'object': tag, 'location': reader}
            print(tag, reader)
            reader_current = reader

            if reader == 'reader0':
                with lock:
                    object_correct, location_start, location_correct = retrieve_tag(
                        tag_dict)  # the object the robot identifies to be placed
                    tag_time = time.time()

            else:
                with lock:
                    object_current, location_current, location_correct = retrieve_tag(tag_dict)
                    tag_time = time.time()

                if not object_correct == object_current:
                    object_current = ''
                    location_current = ''
                    location_correct = ''
                    speech_service.setParameter("speed", speech_rate_base)
                    animated_speech.say(
                        'Bitte stelle ein neues Objekt immer zuerst auf die Start Box, damit ich dir sagen kann wo es hingehoert.')  # the object




def cond_1():

    '''This runs the Pepper behavior for condition 1
   '''

    global object_correct
    global emotion_no
    global behavior
    global joy
    global last_mtime
    global object_current
    global experiment_start_time
    global location_correct
    global location_current
    global object_past
    global object_location_corr
    global behavior_index
    global x_perf
    global placement_no
    global experiment_end
    global readers_correct
    global reader_current
    global motivation_memory

    #time.sleep(0.5)
    print('start of condition loop, object correct', object_correct)

    # Define the interval (in seconds) for the emotion assessment (5 minutes in the experiment case)
    interval1 = constants.t_emotion * 60  # 3 minutes * 60 seconds/minutes for emotion assessment
    interval2 = constants.t_additional * 60  # for additional hint

    current_time = time.time()



    #  additional motivation after placement gap

    if current_time - tag_time >= interval2 and current_time - last_mtime >= interval2:

        # Speak text with animation
        speech_service.setParameter("speed", speech_rate_base)
        robot_speech(robot_text.robot_con11)
        last_mtime = time.time()


    # Check if it's time to perform the emotion assessment


    if current_time - experiment_start_time >= interval1:


        # Update the start time for the next interval

        experiment_start_time = current_time

        # run through emotion assessment
        robot_speech(robot_text.robot_con12)
        joy, bored, frust = emotion_assessment()
        robot_speech(robot_text.robot_con13)

        emotion_no += 1
        print(emotion_no)
        print('The emotion assessment is number: ', emotion_no)
        # END OF EMOTION ASSESSMENT

    # Object identification


    if object_correct is not None and object_correct != '' and object_correct != object_past:

        object_location_corr = object_correct + ' ' + location_correct

        print('Current object: ', object_correct, 'Correct location is: ', object_location_corr)

        # speak text with animation
        speech_service.setParameter("speed", speech_rate_base)
        robot_speech(robot_text.robot_con14)
        time.sleep(0.5)
        speech_service.setParameter("speed", speech_rate_swahili)
        animated_speech.say(object_correct) # the object
        speech_service.setParameter("speed", speech_rate_base)
        robot_speech(robot_text.robot_con15)
        speech_service.setParameter("speed", speech_rate_swahili)
        words = object_location_corr.split()
        for word in words:
            animated_speech.say(word) # where to place it
        speech_service.setParameter("speed", speech_rate_base)

        object_past = object_correct

        # Initial word said
        # update  occurrence memory :
        constants.memory_occurrence[object_correct] += 1
        # update associated memory :
        constants.memory_association[object_correct] += 1

        # Word (known) and location (unknown)
        words_in_location = location_correct.split()
        # update occurrence memory :
        for word in words_in_location:
            if word in constants.memory_occurrence:
                # Increment word count for each word in memory
                constants.memory_occurrence[word] += 1
        # update associated memory :
        constants.memory_association[object_correct] += 1

    # End od object identification


    # decide if location CORRECT or INCORRECT

    if object_current == object_correct and object_current != '':  # the current object detected on the readert you can add an action if the object was changed
        object_location = object_current + ' ' + location_current
        #print('Current object is: ', object_current, 'Current location is: ', location_current,
              #  'Current combi is: ', object_location, 'Correct location is: ', location_correct)

        constants.memory_placements = np.append(constants.memory_placements, object_location)

        if object_location_corr == object_location:
            perf_score = 1
            placement_no += 1
            print('The placement number is: ', placement_no)
            x_perf += 1

            behavior_index = np.append(behavior_index, behavior) # save current behavior
            readers_correct = np.append(readers_correct, reader_current) # save current reader in the correct reader list

            constants.memory_performance = np.append(constants.memory_performance, perf_score)

            print('THIS IS A CORRECT LOCATION!', object_location, location_correct)

            # speak text with animation
            speech_service.setParameter("speed", speech_rate_base)
            robot_speech(robot_text.robot_con16)
            speech_service.setParameter("speed", speech_rate_swahili)
            words = object_location.split()
            for word in words:
                animated_speech.say(word)
            speech_service.setParameter("speed", speech_rate_base)
            robot_speech(robot_text.robot_con17)

            # updated occurrence memory
            words_in_location = object_location.split()
            for word in words_in_location:
                if word in constants.memory_occurrence:
                    # Increment word count for each word in memory
                    constants.memory_occurrence[word] += 1
            # update associated memory
            for word in words_in_location:
                if word in constants.memory_association:
                    # Increment word count for each word in memory
                    constants.memory_association[word] += 1





        else:
            perf_score = -1
            placement_no += 1
            print('The placement number is: ', placement_no)
            x_perf += -1


            constants.memory_performance = np.append(constants.memory_performance, perf_score)

            # speak text with animation
            speech_service.setParameter("speed", speech_rate_base)
            robot_speech(robot_text.robot_con18)
            speech_service.setParameter("speed", speech_rate_swahili)
            words = object_location.split()
            for word in words:
                animated_speech.say(word)
            speech_service.setParameter("speed", speech_rate_base)
            robot_speech(robot_text.robot_con19)
            speech_service.setParameter("speed", speech_rate_swahili)
            object_location_correct = object_current + location_correct
            words = object_location_correct.split()
            for word in words:
                animated_speech.say(word)
            speech_service.setParameter("speed", speech_rate_base)


            # update occurrence memory
            words_in_location = object_location.split()
            for word in words_in_location:
                if word in constants.memory_occurrence:
                    # Increment word count for each word in memory
                    constants.memory_occurrence[word] += 1
            # update associated memory
            for word in words_in_location:
                print('THIS IS A WORD in object location', word)
                if word in constants.memory_association:
                    print('THIS IS A WORD ADDED TO ASSOCIATION MEMORY', word)
                    # Increment word count for each word in memory
                    constants.memory_association[word] += 1

            # update occurrence memory
            words_in_location = object_location_correct.split()
            for word in words_in_location :
                if word in constants.memory_occurrence:
                    # Increment word count for each word in memory
                    constants.memory_occurrence[word] += 1
            # update associated memory
            constants.memory_association[object_current] += 1


            # COND 2: add random hint from table 1

            # hintn = random.randrange(20)  # random integer from 0 to 19
            # hint = hint = robot_text.robot_con20[hintn]
            # speech_service.setParameter("speed", speech_rate_base)
            # robot_speech(hint)
            # print(hint)

            # COND 3: add hint from table 1 X% of the time
            print('emotion number', emotion_no)
            if emotion_no >= 1:


                global joy
                i = random.randrange(100)  # get random integer between 0 and 100

                if x_perf / placement_no <= 0.5:  # RED side of behaviors
                    print('the performance score is: ', x_perf / placement_no)
                    if joy > 3:  # BEHAVIOR 4: hints after 60% of placements
                        behavior = 4
                        behavior_index = np.append(behavior_index, behavior)
                        print('BEH4')
                        if i <= 60:  # in 60 % of placements
                            print('additional hint given')
                            hintn = random.randrange(20)  # random integer from 0 to 19
                            hint = robot_text.robot_con20[hintn]
                            while hint == hint_memory[-1]:  # avoid same hint being used twice
                                hintn = random.randrange(20)
                                hint = robot_text.robot_con20[hintn]

                            speech_service.setParameter("speed", speech_rate_base)
                            robot_speech([hint])
                            hint_memory = np.append(hint_memory, placement_no)
                            hint_memory = np.append(hint_memory, hint)
                            print('The hints given so far: ', hint_memory)
                                # print(hint)
                    elif joy == 3:  # BEHAVIOR 5: hints after 80% of placements
                        behavior = 5
                        behavior_index = np.append(behavior_index, behavior)
                        print('BEH5')

                        if i <= 80:  # in 80 % of placements
                            print('additional hint given')
                            hintn = random.randrange(20)  # random integer from 0 to 19
                            hint = robot_text.robot_con20[hintn]
                            while hint == hint_memory[-1]:  # avoid same hint being used twice
                                hintn = random.randrange(20)
                                hint = robot_text.robot_con20[hintn]
                            speech_service.setParameter("speed", speech_rate_base)
                            robot_speech([hint])
                            hint_memory = np.append(hint_memory, placement_no)
                            hint_memory = np.append(hint_memory, hint)
                                # print(hint)
                    else:  # BEHAVIOR 6: hints after all placements
                        print('BEH6')
                        behavior = 6
                        behavior_index = np.append(behavior_index, behavior)
                        print('additional hint given')
                        hintn = random.randrange(20)  # random integer from 0 to 19
                        hint = robot_text.robot_con20[hintn]
                        while hint == hint_memory[-1]:  # avoid same hint being used twice
                            hintn = random.randrange(20)
                            hint = robot_text.robot_con20[hintn]
                        speech_service.setParameter("speed", speech_rate_base)
                        robot_speech([hint])
                        hint_memory = np.append(hint_memory, placement_no)
                        hint_memory = np.append(hint_memory, hint)


                else:  # GREEN side of behaviors
                    print('the performance score is: ', x_perf / placement_no)
                    if joy >= 3:  # BEHAVIOR 1: no hints
                        print('BEH1')
                        behavior = 1
                        behavior_index = np.append(behavior_index, behavior)
                    elif joy == 3:  # BEHAVIOR 2: hints after 20% of placements and engaging message if prior in behavior 1
                        print('BEH2')

                        if i <= 20:  # hint in 20 % of placements
                            print('additional hint given')
                            hintn = random.randrange(20)  # random integer from 0 to 19
                            hint = robot_text.robot_con20[hintn]
                            while hint == hint_memory[-1]:  # avoid same hint being used twice
                                hintn = random.randrange(20)
                                hint = robot_text.robot_con20[hintn]
                            speech_service.setParameter("speed", speech_rate_base)
                            robot_speech([hint])
                            hint_memory = np.append(hint_memory, placement_no)
                            hint_memory = np.append(hint_memory, hint)
                            # print(hint)

                            if behavior == 1:  # motivational message
                                hintn = random.randrange(16)  # random integer from 0 to 15
                                hint = robot_text.robot_con30[hintn]
                                speech_service.setParameter("speed", speech_rate_base)
                                robot_speech([hint])

                                motivation_memory = np.append(motivation_memory, placement_no)
                                motivation_memory = np.append(motivation_memory, hint)

                        behavior = 2
                        behavior_index = np.append(behavior_index, behavior)



                    else:  # BEHAVIOR 3: hints after all placements

                        print('BEH3')

                        if i <= 40:  # hint in 40 % of placements
                            print('additional hint given')
                            hintn = random.randrange(20)  # random integer from 0 to 19
                            hint = robot_text.robot_con20[hintn]
                            while hint == hint_memory[-1]:  # avoid same hint being used twice
                                hintn = random.randrange(20)
                                hint = robot_text.robot_con20[hintn]
                            speech_service.setParameter("speed", speech_rate_base)
                            robot_speech([hint])
                            hint_memory = np.append(hint_memory, placement_no)
                            hint_memory = np.append(hint_memory, hint)
                            # print(hint)

                            if behavior == 1 or behavior == 2:  # engaging message
                                hintn = random.randrange(16)  # random integer from 0 to 15
                                hint = robot_text.robot_con30[hintn]
                                speech_service.setParameter("speed", speech_rate_base)
                                robot_speech([hint])

                                motivation_memory = np.append(motivation_memory, placement_no)
                                motivation_memory = np.append(motivation_memory, hint)

                        behavior = 3
                        behavior_index = np.append(behavior_index, behavior)

                    # END of COND 3

    with lock:
        object_current = ''

    current_time = time.time()
    if current_time > experiment_end_time or len(readers_correct) == 16:
        np.save('behaviors', behavior_index)
        np.save('placement_no', placement_no)
        np.save('performance', constants.memory_performance)
        np.save('placements', constants.memory_placements)
        np.save('hints', hint_memory)
        np.save('motivational', motivation_memory)
        file_path = 'occurrence_memory'
        with open(file_path, 'w') as json_file:
            json.dump(constants.memory_occurrence, json_file)
        file_path = 'association_memory'
        with open(file_path, 'w') as json_file:
            json.dump(constants.memory_association, json_file)

        #  say end of experiment text
        time.sleep(0.5)
        robot_speech(robot_text.robot_con90)

        experiment_end = True






        # save outputs STILL NEED TO FIGURE OUT BEST WAY TO SAVE THESE AT FINAL STAGE

def retrieve_tag(tag_data):

    '''This function maps the tag data to the locations and objects.
        It provides the object detected on the reader and which location the reader is in.'''

    object_ID = tag_data['object']
    location_ID = tag_data['location']

    print('The current object ID is:', object_ID)
    print('The current location ID is: ', location_ID)
    object_cur = constants.tag_to_object_mapping[object_ID][0]
    location_cur = constants.tag_to_location_mapping.get(location_ID, None)
    location_cor = constants.tag_to_object_mapping[object_ID][1]
    print('The object recognised is: ', object_cur)
    print('The current location is: ', location_cur)
    #time.sleep(1)
    return object_cur, location_cur, location_cor


def extract_identifiers(data):

    '''This function formats the tag id to Python readable format.'''

    # Split the data by comma
    tag_and_reader = data.split(', ')

    # Extract values
    if len(tag_and_reader) == 2:
        tag_no = tag_and_reader[0].strip()
        reader_no = tag_and_reader[1].strip()

        #print("Tag:", tag_no)
        #print("Reader:", reader_no)
    else:
        #print("Invalid data format.")
        tag_no = ''
        reader_no = ''

    return tag_no, reader_no

if __name__ == "__main__":


    # GLOBAL VARIABLES initialization

    global object_current
    global location_current
    global tag_time
    global location_correct
    global experiment_start_time
    global experiment_end_time
    global last_mtime
    global emotion_no
    global behavior
    global joy
    global object_correct
    global object_past
    global behavior_index
    global x_perf
    global placement_no
    global experiment_end
    global hint_counter
    global readers_correct
    global reader_current
    global hint_memory
    global motivation_memory
    global prev_loc_check

    object_current = ''
    object_correct = ''
    object_past = ''
    location_current = ''
    location_correct = ''
    tag_time = time.time()
    experiment_start_time = time.time()
    last_mtime = time.time()
    experiment_end_time = experiment_start_time + 30 * 60  # 30 minutes * 60 seconds/min
    emotion_no = 0
    behavior = 1  # initialization that is not 1 or 2
    joy = 0
    behavior_index = []
    # scores for percentage X of extra hint
    placement_no = 0
    x_perf = 0
    experiment_end = False
    hint_counter = 0
    readers_correct = np.array([])
    reader_current = ''
    hint_memory = np.array([''])
    motivation_memory = np.array([])
    prev_loc_check = ''

    # Create a lock to synchronize access to the shared variable
    lock = threading.Lock()

    # !!! PEPPER RELATED !!!

    # set speech rate

    speech_rate_base = constants.speech_rate_base
    speech_rate_swahili = constants.speech_rate_swahili

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
    tracker_service = session.service("ALTracker")

    ## Get the ALAnimatedSpeech service
    animated_speech = session.service("ALAnimatedSpeech")  # says a text and animates it with movements
    speak_move_service = session.service("ALSpeakingMovement")

    # close running behaviors
    close_running_behavs()

    ## Start active tracking

    behavior_mng_service.runBehavior('p50_study1-5ba9db/basic_awareness_ON', _async=True)

    # !!!  PEPPER RELATED  !!!



    # !!! NFC CONNECTION !!!

    # Define the number of ports
    num_ports = constants.n_ports

    # Create a dictionary to store the serial ports
    reader_ports = {}

    # define the serial ports
    for i in range(0, num_ports):
        port_name = '/dev/ttyUSB{}'.format(i)
        reader_ports['reader{}_port'.format(i)] = serial.Serial(port_name, 9600, timeout=1)
        # print(port_name)

    # wait for the port to open
    time.sleep(1.5)

    while not experiment_end:
        # Create threads
        thread1 = threading.Thread(target=detect_nfc_tags_parallel)
        thread2 = threading.Thread(target=cond_1)
        # thread3 = threading.Thread(target=check_incorrect_placements)

        # Start threads
        thread1.start()
        thread2.start()
        # thread3.start()

        # Wait for threads to finish
        thread1.join()
        thread2.join()
        # thread3.join()

    # Close the serial port when done (needs to happen after experiment end time, then play end of experiment code
    for port_name, port in reader_ports.items():
        port.close()

    close_running_behavs()

    # !!! NFC CONNECTION !!!





