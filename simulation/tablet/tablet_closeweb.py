import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import qi
import constants



def main(session):
    signalID = 0
    try:
        # Get the tablet service
        tablet_service = session.service("ALTabletService")

        tablet_service.hideWebview()
        tabletService.onJSEvent.disconnect(signalID)

    except Exception, e:
        print
        "Error was: ", e


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

    main(session)
