
import sys
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
from german.behaviors import constants
from twisted.internet import reactor
import random



def detect_simulated_nfc_tags():
    # generate a random number between 0 and 1
    random_number = random.random()

    # get the defined objects and locations
    object_list = constants.objects_en
    location_list = constants.reader_nr
    correct_location = constants.positions_cor

    # set the rate at which correct decisions are made
    treshold = 0.5

    # Simulate NFC tag detection
    if random_number < treshold:
        # simulate a correct choice
        object = random.choice(object_list)
        location = object_list.index(object)
        tag_data = {'object': object, 'location': location}
        print("NFC Tag detected is a correct placement:", tag_data)


    else:
        # simulate an incorrect (random) choice
        tag_data = {'object': random.choice(object_list), 'location': random.choice(location_list)}
        print("NFC Tag detected is an incorrect placement:", tag_data)



    # Call the function to process the detected tag data
    process_detected_tags(tag_data)

    # Schedule the next detection after a 5-second interval
    reactor.callLater(5, detect_simulated_nfc_tags)


def process_detected_tags(tag_data):
    # retrieve object and location from tag
    object_current = tag_data.get("object")
    location_index = int(tag_data.get('location'))
    print('The current location is: ', location_index)
    print('The current object is: ', object_current)
    location_current = constants.positions_cor[int(location_index)]
    object_location = object_current + ' ' + location_current
    print('The object is currently in:', object_location)
    location_correct = constants.objects_location[constants.objects_en.index(object_current)]
    print('The object should be in: ', location_correct)
    if object_location == location_correct:
        print('THIS IS A CORRECT LOCATION!', object_location, location_correct)





if __name__ == "__main__":
    # set speech rate


    # Start the tag detection
    reactor.callLater(0, detect_simulated_nfc_tags)

    # Start the reactor to run the Twisted event loop
    reactor.run()