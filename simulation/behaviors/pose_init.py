import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
import qi
import constants



def main(session):
    """
    Use the goToPosture Method to PoseZero.
    Set all the motors of the body to zero.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")



    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand Zero
    posture_service.goToPosture("StandInit", 0.5)

    # We use the "Body" name to signify the collection of all joints and actuators
    #pNames = "Body"

    # Get the Number of Joints
    #numBodies = len(motion_service.getBodyNames(pNames))

    # We prepare a collection of floats
    #pTargetAngles = [0.0] * numBodies

    # We set the fraction of max speed
    #pMaxSpeedFraction = 0.3

    # Ask motion to do this with a blocking call
    #motion_service.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)

    # Go to rest position
    #motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=constants.ip,
                        help="Robot IP address, specified in the constants.")
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

main(session)