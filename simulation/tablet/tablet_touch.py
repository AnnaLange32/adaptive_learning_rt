import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import constants
import qi

def touch(app):
    """
    This example uses the onTouchDown method.
    It separates the screen into separate areas.
    It provides a different input code for each touched area.
    This script needs to be run ON the robot.

    """

    answer = [0] #holder for participant answer

    try:
        session = app.session
        tabletService = session.service("ALTabletService")

        # Don't forget to disconnect the signal at the end
        signalID = 0

        # function called when the signal onTouchDown is triggered
        def callback(self,x, y):
            print "coordinates are x: ", x, " y: ", y
            if x < 400: # specify horizontal limit of touchzone, y coord can be added
                answer[0] = 1 # specify the output associated to the area
                print('I was touched')  # can be removed
                tabletService.onTouchDown.disconnect(signalID)

                # disconnect the signal

            elif x < 800:  # add further zones as required...
                answer[0] = 2 # assign further outputs...
                print('I was touched')  # can be removed
                tabletService.onTouchDown.disconnect(signalID)


            elif x < 1200:
                answer[0] = 3
                print('I was touched')  # can be removed
                tabletService.onTouchDown.disconnect(signalID)


            elif x < 1600:
                answer[0] = 4
                print('I was touched')  # can be removed
                tabletService.onTouchDown.disconnect(signalID)


            elif x < 2000:
                answer[0] = 5
                print('I was touched')  # can be removed
                tabletService.onTouchDown.disconnect(signalID)

            # disconnect the signal
            app.stop()

        # attach the callback function to onJSEvent signal


        signalID = tabletService.onTouchDown.connect(callback)

        app.run()

    except Exception, e:
        print "Error was: ", e

    print('The given answer was: ', answer) # provides running output, can be removed

    return answer



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=constants.ip,
                        help="Robot IP address.")
    parser.add_argument("--port", type=int, default=constants.port,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["TabletModule", "--qi-url=" + connection_url])
        app.start()
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(app)
