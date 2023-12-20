
"""Example: PoseInit - Small example to make Nao go to an initial position."""


import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
from naoqi import ALProxy



def main(session):
    """
    Use the goToPosture Method to PoseZero.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_proxy = ALProxy("ALMotion", args.ip, args.port)
    posture_proxy = ALProxy("ALRobotPosture", args.ip, args.port)

    # Wake up robot
    motion_proxy.wakeUp()

    # Send robot to Stand Init
    posture_proxy.goToPosture("StandZero", 0.5)

    # Go to rest position
    motion_proxy.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()

    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)