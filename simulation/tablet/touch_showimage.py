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

'''This script is currently not going to be used as the robot cannot access the remote images.'''
def main(session, app):
    """
    This example uses the showImage method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.
    answer = [0]  # holder for participant answer
    def log_execution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            function_name = func.__name__
            logging.info("{0}, {1}".format(args, function_name))
            result = func(*args, **kwargs)
            logging.info("{0}, {1}".format(result, function_name))
            return result

        return wrapper

    try:

        print(tabletService, type(tabletService))
        print(help(tabletService.showImage))
        tabletService.showImage('http://198.18.0.1/apps/anna-89e97e/enjoyment.png') #https://i.imgur.com/w01EMeD.png


        session2 = app.session
        tabletService2 = session2.service("ALTabletService")

        # Don't forget to disconnect the signal at the end
        signalID = 0

        # function called when the signal onTouchDown is triggered
        def callback(x, y):
            print "coordinate are x: ", x, " y: ", y
            if x < 400:  # specify horizontal limit of touchzone, y coord can be added
                answer[0] = 1  # specify the output associated to the area
            elif x < 800:  # add further zones as required...
                answer[0] = 2  # assign further outputs...
            elif x < 1200:
                answer[0] = 3
            elif x < 1600:
                answer[0] = 4
            elif x < 2000:
                answer[0] = 5
            # disconnect the signal
            tabletService2.onTouchDown.disconnect(signalID)
            print('I was touched')  # provides running output, can be removed
            app.stop()

            # attach the callback function to onJSEvent signal
            signalID = tabletService2.onTouchDown.connect(callback)
            app.run()

        print('The given answer was: ', answer)  # provides running output, can be removed

        time.sleep(10)

         # Hide the web view
        tabletService.hideImage()

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
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["TabletModule", "--qi-url=" + connection_url])
        app.start()
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
tabletService = session.service("ALTabletService")
tabletService.preLoadImage('http://198.18.0.1/apps/anna-89e97e/enjoyment.png')  #http://198.18.0.1/apps/anna-89e97e/enjoyment.png'
main(session, app)