import argparse
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import constants
import qi
from tablet_touch import *
from tablet_showimage import *
import numpy as np

def emotion_questionnaire():

    answers = np.zeros(3)

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=constants.ip,
                        help="Robot IP address.")
    parser.add_argument("--port", type=int, default=constants.port,
                        help="Naoqi port number")
    args = parser.parse_args()

    # Initialize qi.Session
    session = qi.Session()
    session.connect("tcp://" + args.ip + ":" + str(args.port))
    # Initialize qi.Application
    connection_url = "tcp://" + args.ip + ":" + str(args.port)
    #app = qi.Application(["TabletModule", "--qi-url=" + connection_url])



    for n, emotion in enumerate(constants.emotions):

        app = qi.Application(["TabletModule", "--qi-url=" + connection_url])

        app.start()
        filepath = 'http://198.18.0.1/apps/anna-89e97e/' + emotion + '.png'
        print(n)
        print(filepath)


        show_image(session, filepath)
        time.sleep(4)
        answers[n] = touch(app)[0]
        print(answers)
    return answers



emotion_questionnaire()