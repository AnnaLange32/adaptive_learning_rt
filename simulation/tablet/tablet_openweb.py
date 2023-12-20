import sys
import argparse
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/helpers')
import qi
import constants



def main(session, url):
    try:
        # Get the tablet service
        tablet_service = session.service("ALTabletService")
        print(tablet_service, type(tablet_service))

        tablet_service.showWebview(url)


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
    default_url = 'https://i.imgur.com/w01EMeD.png'#"http://198.18.0.1/apps/anna-89e97e/enjoyment.png"#"192.168.0.141/img/help_charger.png"#'https://no4gujj33sf.typeform.com/to/sNELUpEa' #'http://doc.aldebaran.com/2-4/naoqi/core/altabletservice-api.html?highlight=getwifi'
    main(session, default_url)
