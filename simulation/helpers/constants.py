


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
#swahili words adjusted for correct pronounciation
objects_sw = ["tschupa", "kitaabu", "savaadi", "ssimu", 'hmmmmmto', "kiaatu", "kalaamu", "mfuko", "pootschi", "assaali", "kikoombe", "tufaha"]

#swahili words adjusted for correct pronounciation
locations_sw =   ["meessa", "kiti", "raafu", "dirihscha", "ssanduku", "kinjessi", "utschorahi"]
prepositions_sw = ["kwenje", "tschini ja", "mmmmmbaehlea?", "njuma ja", "karibuhna?"]

position_ger = ['auf Tisch', 'unter Tisch', 'auf Stuhl', 'unter Stuhl', 'auf Regal', 'vor Regal', 'neben Regal', 'vor Fenster', 'unter Fenster', 'hinter Kiste', 'neben Kiste', 'neben Hocker', 'unter Hocker', 'hinter Bild', 'vor Bild']
position_sw = ['kwenje meessa', 'tschini ja meessa', 'kwenje kiti', 'tschini ja kiti', 'kwenje raafu', 'mmmmmbaehlea? raafu', 'karibuhna? raafu', 'mmmmmbaehlea? dirihscha', 'tschini ja dirihscha', 'njuma ja ssanduku', 'karibuhna? ssanduku', 'karibuhna? kinjessi', 'tschini ja kinjessi', 'njuma ja utschorahi', 'mmmmmbaehlea? utschorahi']

# vocab for simulation only

objects_location = ['Flasche auf Regal', 'Buch neben Kiste', 'Geschenk vor Fenster', 'Telefon neben Hocker', 'Kissen vor Regal', 'Schuh hinter Kiste', 'Stift auf Tisch', 'Tasche auf Stuhl', 'Geldbeutel unter Hocker', 'Honig hinter Bild', 'Tasse unter Stuhl', 'Apfel unter Tisch']
positions_cur = ['auf Regal', 'neben Kiste', 'vor Fenster', 'neben Hocker', 'vor Regal', 'hinter Kiste', 'auf Tisch', 'auf Stuhl', 'unter Hocker', 'hinter Bild', 'unter Stuhl', 'unter Tisch']  # needed for simulation
positions_cur_sw = ['kwenje raafu', 'njuma ja ssanduku', 'mmmmmbaehlea? dirihscha', 'tschini ja kinjessi', 'mmmmmbaehlea? raafu', 'njuma ja ssanduku', 'kwenje meessa', 'kwenje kiti', 'tschini ja kinjessi', 'njuma ja utschorahi', 'tschini ja kiti', 'tschini ja meessa']

# Initialize the empty robot memory (dictionary or list)
memory_occurence = {'tschini ja': 0, "kinjessi": 0, "ssimu": 0, 'kiti': 0, "kiaatu": 0, "tschupa": 0, "kalaamu": 0, "dirihscha": 0, "njuma ja": 0, "assaali": 0,  "kitaabu": 0, "kwenje": 0, "ssanduku": 0, "tufaha": 0, "mmmmmbaehlea?": 0, "mfuko": 0,  "savaadi": 0, "utschorahi": 0, "karibuhna?": 0, "kikoombe": 0, "raafu": 0, "meessa": 0, 'hmmmmmto': 0, "pootschi": 0}
 # in this memory the robot remembers each word it has told the participant in swahili and the number of occurences
memory_association ={'tschini ja': 0, "kinjessi": 0, "ssimu": 0, 'kiti': 0, "kiaatu": 0, "tschupa": 0, "kalaamu": 0, "dirihscha": 0, "njuma ja": 0, "assaali": 0,  "kitaabu": 0, "kwenje": 0, "ssanduku": 0, "tufaha": 0, "mmmmmbaehlea?": 0, "mfuko": 0,  "savaadi": 0, "utschorahi": 0, "karibuhna?": 0, "kikoombe": 0, "raafu": 0, "meessa": 0, 'hmmmmmto': 0, "pootschi": 0} # here the robot only remembers the words for which meaning could be deducted by participants
memory_performance =  [] # here the robot remembers the placements 1 for a correct placement and -1 for an incorrect one


# Initialize the memory for the simulation

smemory_occurence = {'unter': 0, 'Hocker': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_association = {'unter': 0, 'Hocker': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_performance = []