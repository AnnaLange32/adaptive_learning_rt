


#robot Ip and Port

ip = '192.168.0.141'

port = 9559


# the variables for the emotion questionnaire

emotions = ['enjoyment', 'frustration', 'boredom']


# positions of nfc readers

reader_nr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#position_en = ['on desk', 'under desk', 'next to desk', 'on drawer', 'under drawer', 'next to drawer', 'on sideboard', 'under sideboard', 'next to sideboard', 'on chair', 'under chair', 'next to chair', 'on shelf', 'under shelf', 'next to shelf']
position_su = []  # tbc: positions in swahili


# required vocabulary

objects_de = ['Flasche', 'Buch', 'Geschenk', 'Telefon', 'Kissen', 'Schuh', 'Stift', 'Tasche', 'Geldbeutel', 'Honig', 'Tasse', 'Apfel']
objects_en = ['bottle', 'book', 'present', 'telephone', 'pillow', 'shoe', 'pen', 'bag', 'wallet', 'honey', 'cup', 'apple']
objects_sw = ["chupa", "kitabu", "zawadi", "simu", "mto", "kiatu", "kalamu", "mfuko", "pochi", "asali", "kikombe", "tufaha"]

locations_sw =  ["meza", "kiti", "rafu", "dirisha", "sanduku", "kinyesi", "uchoraji"]
prepositions_sw = ["kwnye", "chini ya", "mbele ya", "nyuma ya", "karibu na"]

position_ger = ['auf Tisch', 'unter Tisch', 'auf Stuhl', 'unter Stuhl', 'auf Regal', 'vor Regal', 'neben Regal', 'vor Fenster', 'unter Fenster', 'hinter Kiste', 'neben Kiste', 'neben Hocker', 'unter Hocker', 'hinter Bild', 'vor Bild']
position_su = ['kwenye meza', 'chini ya meza', 'kwenye kiti', 'chini ya kiti', 'kwenye rafu', 'mbele ya rafu', 'karibu ya rafu', 'mbele ya dirisha', 'chini ya dirisha', 'nyuma ya sanduku', 'karibu ya sanduku', 'karibu ya kinyesi', 'chini ya kinyesi', 'nyuma ya uchoraji', 'mbele ya uchoraji']


# vocab for simulation only

objects_location = ['Flasche auf Regal', 'Buch neben Kiste', 'Geschenk vor Fenster', 'Telefon neben Hocker', 'Kissen vor Regal', 'Schuh hinter Kiste', 'Stift auf Tisch', 'Tasche auf Stuhl', 'Geldbeutel unter Hocker', 'Honig hinter Bild', 'Tasse unter Stuhl', 'Apfel unter Tisch']
positions_cur = ['auf Regal', 'neben Kiste', 'vor Fenster', 'neben Hocker', 'vor Regal', 'hinter Kiste', 'auf Tisch', 'auf Stuhl', 'unter Hocker', 'hinter Bild', 'unter Stuhl', 'unter Tisch']  # needed for simulation


# Initialize the empty robot memory (dictionary or list)
memory_occurence = {'chini ya': 0, 'kinyesi': 0, 'simu': 0, 'kiti': 0, 'kiatu': 0, 'chupa': 0, 'kalamu': 0, 'dirisha': 0, 'nyuma ya': 0, 'asali': 0, 'kitabu': 0, 'kwnye': 0, 'sanduku': 0, 'tufaha': 0, 'mbele ya': 0, 'mfuko': 0, 'zawadi': 0, 'uchoraji': 0, 'karibu na': 0, 'kikombe': 0, 'rafu': 0, 'meza': 0, 'mto': 0, 'pochi': 0}
 # in this memory the robot remembers each word it has told the participant in swahili and the number of occurences
memory_association = {} # here the robot only remembers the words for which meaning could be deducted by participants
memory_performance =  [] # here the robot remembers the placements 1 for a correct placement and -1 for an incorrect one


# Initialize the memory for the simulation

smemory_occurence = {'unter': 0, 'Hocker': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_association = {'unter': 0, 'Hocker': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_performance = []


#NFC_tags remove lehrzeichen

a = '04 8D C1 72 B8 72 80'
b = '04 91 C1 72 B8 72 80'
c = '\x000 04 A1 C1 72 B8 72 80'
d = '04 95 C1 72 B8 72 80'
e = '\xfd 04 9D C1 72 B8 72 80'
f = 'd\xe5\r\n'
g = '\x000 04 86 C0 72 B8 72 80'
h = '04 A8 C0 72 B8 72 80'
i = '04 8A C0 72 B8 72 80'

