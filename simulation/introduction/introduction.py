# -*- coding: iso-8859-1 -*-
import sys
sys.path.append("/home/anna/.virtualenvs/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
sys.path.append('/home/anna/PycharmProjects/PT_cond1/german/helpers')
import time
import qi
import constants


# Define the robot's IP address and port
robot_ip = constants.ip
port = constants.port

close_running_behavs()

# Text to be spoken
text_to_say1 = ("^mode(cotextual) Hi, ich bin Pepper und ich werde heute dein Lehrer sein.")
text_to_say2 = (" ^mode(disabled) Ich freue mich sehr, ^mode(contextual) dass du hier bist und ^mode(disabled) wir gemeinsam ein Spiel spielen werden!")
text_to_say3 = (" ^mode(random) Meine Kollegin hat dir sicher schon ein wenig erzaehlt, ^mode(disabled) aber ich ^mode(contextual) erklaere dir das Spiel gerne nochmal.") # ^start(p50_study1-5ba9db/behavior 1)
text_to_say4 = ("Wie du sehen kannst, gibt es in diesem Raum viele Gegenstaende.")
text_to_say5 = ("^mode(disabled) Deine Aufgabe wird es sein, diese Gegenstaende an bestimmten Stellen hier im Raum zu positionieren.")
text_to_say6 = ("^mode(contextual) Moegliche Stellen erkennst du an kleinen, weissen Boxen,")
text_to_say7 = ("wie zum Beispiel dieser hier. ") #^start(p50_study1-5ba9db/behavior 2).
text_to_say8 = ("^mode(contextual)  Wie du siehst, sind diese im ganzen Raum verteilt.  Bitte stelle ^mode(disabled)  Objekte auch wirklich immer nur auf diese Boxen.  ^mode(contextual) Alles andere waere keine richtige Platzierung. ^mode(disabled) Ausserdem, kann ich dir sonst kein Feedback geben.")
text_to_say9 = ("^mode(contextual) Jeder Gegenstand hat genau eine korrekte Position und dein Ziel ist es, diese herauszufinden und den Gegenstand auch dort zu platzieren.")
text_to_say10 = ("Soweit klar, oder?") #^start(p50_study1-5ba9d# b/behavior 3).
text_to_say11 = (" ^mode(disabled) Damit es aber nicht zu einfach fuer dich ist, werde ich ^mode(contextual) dir in einer Fremdsprache sagen, wo du die Gegenstaende hinstellen musst. ^mode(contextual) Und zwar in Swahili - einer Sprache, die in vielen Laendern Ost- und Zentralafrikas, ^mode(disabled) wie Kenia und Tansania, gesprochen wird.")
text_to_say12 = (" ^mode(disabled) Aber keine Sorge wenn du gar keine Ahnung von Swahili hast. ^mode(contextual)  Das ist sogar wichtig, damit das Spiel richtig funktioniert und du auch ein bisschen raetseln musst.  ^mode(disabled) Aber lass mich dir ein paar Beispiele geben, damit du verstehst, wie es ablaufen wird.")

# Speech rate (adjust to change speed)

speech_rate = 85

# Connect to the robot
session = qi.Session()
session.connect("tcp://" + robot_ip + ":" + str(port))


# Get the ALMotion service
motion_service = session.service("ALMotion")
speech_service = session.service("ALTextToSpeech")
posture_service = session.service("ALRobotPosture")
behavior_mng_service = session.service("ALBehaviorManager")

## Get the ALAnimatedSpeech service
animated_speech = session.service("ALAnimatedSpeech") #says a text and animates it with movements
speak_move_service = session.service("ALSpeakingMovement")
posture_service.goToPosture("StandInit", 0.5)
speech_service.setParameter("speed", speech_rate)

# Speak the text with animation
animated_speech.say(text_to_say1)
time.sleep(2)
animated_speech.say(text_to_say2)
time.sleep(1.5)
animated_speech.say(text_to_say3)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 1', _async=True)
time.sleep(2)
animated_speech.say(text_to_say4)
time.sleep(2.5)
animated_speech.say(text_to_say5)
time.sleep(2)
animated_speech.say(text_to_say6)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 2', _async=True)
time.sleep(2.5)
animated_speech.say(text_to_say7)
time.sleep(5)
animated_speech.say(text_to_say8)
time.sleep(2)
animated_speech.say(text_to_say9)
behavior_mng_service.runBehavior('p50_study1-5ba9db/behavior 3', _async=True)
time.sleep(2)
animated_speech.say(text_to_say10)
time.sleep(5) #wait for response
animated_speech.say(text_to_say11)
time.sleep(2)
animated_speech.say(text_to_say12)