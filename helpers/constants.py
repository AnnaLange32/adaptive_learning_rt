
# UPDATE PARTICIPANT NUMBER AND CONDITION BEFORE EACH RUN

participant_no = 1
condition = 4


#robot Ip and Port

ip = '192.168.0.104'  # '192.168.0.141' pepper 4, '192.168.0.104' pepper 1

port = 9559


# speech rate

speech_rate_base = 89
speech_rate_swahili = 75
# ports

n_ports = 17
items_no = 12
experiment_time = 30


# the variables for the emotion questionnaire

emotions = ['enjoyment', 'frustration', 'boredom']
t_emotion = 5 # time in minutes between emotion assessment
t_additional = 1 # time in minutes until additional motivation


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
locations_sw =   ["meessa", "kiti", "raafu", "dirihscha", "ssanduku", "mmmheea", "utschorahi"]
prepositions_sw = ["kwenje", "tschiniija", "mmmmmbaehlea?", "njumaaja", "karibuhna?"]

position_ger = ['auf Tisch', 'unter Tisch', 'auf Stuhl', 'unter Stuhl', 'auf Regal', 'vor Regal', 'neben Regal', 'vor Fenster', 'unter Fenster', 'hinter Kiste', 'neben Kiste', 'neben Pflanze', 'unter Pflanze', 'hinter Bild', 'vor Bild']
position_sw = ['kwenje meessa', 'tschiniija meessa', 'kwenje kiti', 'tschiniija kiti', 'kwenje raafu', 'mmmmmbaehlea? raafu', 'karibuhna? raafu', 'mmmmmbaehlea? dirihscha', 'tschiniija dirihscha', 'njumaaja ssanduku', 'karibuhna? ssanduku', 'karibuhna? mmmheea', 'tschiniija mmmheea', 'njumaaja utschorahi', 'mmmmmbaehlea? utschorahi']

# vocab for simulation only

objects_location = ['Flasche auf Regal', 'Buch neben Kiste', 'Geschenk vor Fenster', 'Telefon neben Pflanze', 'Kissen vor Regal', 'Schuh hinter Kiste', 'Stift auf Tisch', 'Tasche auf Stuhl', 'Geldbeutel unter Pflanze', 'Honig hinter Bild', 'Tasse unter Stuhl', 'Apfel unter Tisch']
positions_cur = ['auf Regal', 'neben Kiste', 'vor Fenster', 'neben Pflanze', 'vor Regal', 'hinter Kiste', 'auf Tisch', 'auf Stuhl', 'unter Pflanze', 'hinter Bild', 'unter Stuhl', 'unter Tisch']  # needed for simulation
positions_cur_sw = ['kwenje raafu', 'njumaaja ssanduku', 'mmmmmbaehlea? dirihscha', 'tschiniija mmmheea', 'mmmmmbaehlea? raafu', 'njumaaja ssanduku', 'kwenje meessa', 'kwenje kiti', 'tschiniija mmmheea', 'njumaaja utschorahi', 'tschiniija kiti', 'tschiniija meessa']

# Initialize the empty robot memory (needs to be one word keys)
memory_occurrence = {'tschiniija': 0, 'ja': 0, "mmmheea": 0, "ssimu": 0, 'kiti': 0, "kiaatu": 0, "tschupa": 0, "kalaamu": 0, "dirihscha": 0, "njumaaja": 0, "assaali": 0,  "kitaabu": 0, "kwenje": 0, "ssanduku": 0, "tufaha": 0, "mmmmmbaehlea?": 0, "mfuko": 0,  "savaadi": 0, "utschorahi": 0, "karibuhna?": 0, "kikoombe": 0, "raafu": 0, "meessa": 0, 'hmmmmmto': 0, "pootschi": 0}
 # in this memory the robot remembers each word it has told the participant in swahili and the number of occurences
memory_association = {'tschiniija': 0,  'ja': 0, "mmmheea": 0, "ssimu": 0, 'kiti': 0, "kiaatu": 0, "tschupa": 0, "kalaamu": 0, "dirihscha": 0, "njumaaja": 0, "assaali": 0,  "kitaabu": 0, "kwenje": 0, "ssanduku": 0, "tufaha": 0, "mmmmmbaehlea?": 0, "mfuko": 0,  "savaadi": 0, "utschorahi": 0, "karibuhna?": 0, "kikoombe": 0, "raafu": 0, "meessa": 0, 'hmmmmmto': 0, "pootschi": 0} # here the robot only remembers the words for which meaning could be deducted by participants
memory_performance = []  # here the robot remembers the placements 1 for a correct placement and -1 for an incorrect one
memory_placements = []  # here the robots remembers past placements incl. object preposition location

# Initialize the memory for the simulation

smemory_occurrence = {'unter': 0, 'Pflanze': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_association = {'unter': 0, 'Pflanze': 0, 'Telefon': 0, 'Stuhl': 0, 'Schuh': 0, 'Flasche': 0, 'Stift': 0, 'Fenster': 0, 'hinter': 0, 'Honig': 0, 'Buch': 0, 'auf': 0, 'Box': 0, 'Apfel': 0, 'vor': 0, 'Tasche': 0, 'Geschenk': 0, 'Bild': 0, 'neben': 0, 'Tasse': 0, 'Regal': 0, 'Tisch': 0, 'Kissen': 0, 'Geldbeutel': 0}
smemory_performance = []


# Create a dictionary to map tag IDs to object and the correct location names for each object
tag_to_object_mapping = {
    "04 FE 8B 3F B9 2A 81": ("tschupa", 'kwenje raafu'), # Flasche + auf Regal
    "04 8D C1 72 B8 72 80": ("kitaabu", 'karibuhna? ssanduku'),  # Buch + neben Kiste
    "04 A8 C0 72 B8 72 80": ("savaadi", 'mmmmmbaehlea? dirihscha'),  # Geschenk + vor Fenster
    "04 9D C1 72 B8 72 80": ("ssimu", 'karibuhna? mmmheea'),  # Telefon + neben Pflanze
    "04 6E 8C 3F B9 2A 81": ("hmmmmmto", 'mmmmmbaehlea? raafu'),  # Kissen + vor Regal
    "04 6F 8C 3F B9 2A 81": ("kiaatu", 'njumaaja ssanduku'),  # Schuh + hinter Kiste
    "04 A1 C1 72 B8 72 80": ("kalaamu", "kwenje meessa"), # Stift + auf Tisch
    "04 8A C0 72 B8 72 80": ("mfuko", "kwenje kiti"), # Tasche + auf Stuhl
    "04 72 8C 3F B9 2A 81": ("pootschi", "tschiniija mmmheea"),  # Geldbeutel + unter Pflanze
    "04 99 C1 72 B8 72 80": ("assaali", 'njumaaja utschorahi'), # Honig + hinter Bild
    "04 FF 8B 3F B9 2A 81": ("kikoombe", 'tschiniija kiti'), # Tasse + unter Stuhl
    "04 71 8C 3F B9 2A 81": ("tufaha", 'tschiniija meessa') # Apfel + unter Tisch

    # Add more tag-object pairs as needed

}

tag_to_location_mapping = {
    "reader0": "Pepper",                   # recognition position
    "reader1": 'kwenje kiti',              # auf Stuhl
    "reader2": 'njumaaja utschorahi',      # hinter Bild
    "reader3": 'karibuhna? raafu',         # neben Regal
    "reader4": 'njumaaja ssanduku',        # hinter Kiste
    "reader5": 'tschiniija dirihscha',     # unter Fenster
    "reader6": 'tschiniija mmmheea',       # unter Pflanze
    "reader7": 'tschiniija kiti',          # unter Stuhl
    "reader8": 'kwenje  ssanduku',         # auf Kiste
    "reader9": 'karibuhna? mmmheea',       # neben Pflanze
    "reader10": "kwenje meessa",           # auf Tisch
    "reader11": 'karibuhna? ssanduku',     # neben Kiste
    "reader12": 'kwenje raafu',            # auf Regal
    "reader13": 'mmmmmbaehlea? dirihscha', # vor Fenster
    "reader14": 'mmmmmbaehlea? utschorahi',# vor Bild
    "reader15": 'mmmmmbaehlea? raafu',     # vor Regal
    "reader16": 'tschiniija meessa'         # unter Tisch

    # Add more tag-object pairs as needed
}