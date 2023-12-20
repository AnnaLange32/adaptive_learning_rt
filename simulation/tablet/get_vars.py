import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")

sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')

import qi
import argparse
import constants



parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, default = constants.ip,
                        help="Robot IP address.")
parser.add_argument("--port", type=int, default=constants.port,
                        help="Naoqi port number")
parser.add_argument("--behavior_name", type=str, default="boot-config/animations/ok",
                    help="Name of the behavior") #--behavior_name

args = parser.parse_args()

session = qi.Session()
try:
    session.connect("tcp://" + args.ip + ":" + str(args.port))
except RuntimeError:
    print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
    sys.exit(1)

memory_service = session.service("ALMemory")

bored = memory_service.getData('P50_study1/variables/bored')

frust = memory_service.getData("P50_study1/variables/frust")

joy = memory_service.getData("P50_study1/variables/joy")

try:
    joy = int(joy)
    bored = int(bored)
    frust = int(frust)

    print('The joy score was: ', joy, ', the bored score was: ', bored, ', the frustration score was: ', frust)
except ValueError:
    # Handle the case where data is not an integer
    print("Data is not an integer")

#print('The values for emotion were: ' , joy, bored, frust)