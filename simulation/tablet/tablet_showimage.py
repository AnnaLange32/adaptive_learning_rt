import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import qi
import time
import constants
import logging
import functools
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#session = qi.Session()
#session.connect("tcp://" + constants.ip + ":" + str(constants.port))


def show_image(session, filepath):
    """
    This example uses the showImage method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    tabletService = session.service("ALTabletService")
    tabletService.preLoadImage(filepath)
    try:
        tabletService.showImage(filepath) #https://i.imgur.com/w01EMeD.png


        #time.sleep(4)

        # Hide the web view
        #tabletService.hideImage()

    except Exception, e:
        print "Error was: ", e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=constants.ip,
                        help="Robot IP address.")
    parser.add_argument("--port", type=int, default=constants.port,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
#tabletService = session.service("ALTabletService")
#filepath = 'http://198.18.0.1/apps/anna-89e97e/enjoyment.png'
#tabletService.preLoadImage(filepath)  #http://198.18.0.1/apps/anna-89e97e/enjoyment.png'
#main(session, filepath)