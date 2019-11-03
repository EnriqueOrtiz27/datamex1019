""" This function clean multiple columns, one at a time. """ 

def clean_first_column(s):
	""" Esta función limpia la primer columna y la deja lista para ser convertida en formato de fecha."""
	
	abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
      'u', 'v', 'x', 'y', 'z']

	ABC = [x.upper() for x in abc]

	s = s.replace(".", "/")
	s = s.replace("/", '')

	for letter in abc:
		s = s.replace(letter, "")

	for letter in ABC:
		s = s.replace(letter, "")

	return s

def clean_reference(s):

	s = str(s)

	s = s.replace("/", "")
	s = s.replace("0", "")
	s = s.replace("1", "")
	s = s.replace("2", "")
	s = s.replace("3", "")
	s = s.replace("4", "")
	s = s.replace("5", "")
	s = s.replace("6", "")
	s = s.replace("7", "")
	s = s.replace("8", "")
	s = s.replace("9", "")
	s = s.replace("%", "")
	

	return s 

def clean_species(s):

	s = str(s)
	s = s.lower()

	if "tiger" in s:
		s = "tiger"
	elif "nurse" in s:
		s = "nurse"
	elif "white" in s:
		s = "white"
	elif "reef" in s:
		s = "reef"
	elif "bull" in s:
		s = "bull"
	elif "lemon" in s:
		s = "lemon"

	elif "angel" in s:
		s = "angel"
	elif "dogfish" in s:
		s = "dog"
	elif "blacktip" in s:
		s = "blacktip"
	elif "sand" in s:
		s = "sandtiger"
	elif "bronze" in s:
		s = "bronze whaler"

	elif "hammerhead" in s:
		s = "hammerhead"
	elif "mako" in s:
		s = "mako"
	elif "raggedtooth" in s:
		s = "raggedtooth"
	elif "sevengill" in s:
		s = "sevengill"
	elif "cookie" in s:
		s = "cookie cutter"

	elif "wobbegong" in s:
		s = "wobbegong"
	elif "sandbar" in s:
		s = "sandbar"
	elif "zambesi" in s:
		s = "zambesi"
	elif "blue" in s:
		s = "blue"
	elif "leopard" in s:
		s = "leopard"

	elif "porbeagle" in s:
		s = "porbeagle"
	elif "galapagos" in s:
		s = "galapagos"
	elif "shovel" in s:
		s = "shovelnose"
	elif "whale" in s:
		s = "whale"
	elif "brown" in s:
		s = "brown"
	else:
		s = "Unregistered"
	
	return s.title() + " Shark"

		


def clean_fatal(s):

	s = str(s)

	if s == " N":
		s = "N"
	elif s == "F":
		s = "UNKNOWN"
	elif s == "N ":
		s = "N"
	elif s == "nan":
		s = "UNKNOWN"
	elif "V" in s:
		s = "UNKNOWN"
	elif s == "n":
		s ="N"

	return s 


def clean_time(s):

	s = str(s)
	s = s.lower()
	s = s.replace("†", ":")
	s = s.replace("h", ":")
	s = s.replace("/", "")
	s = s.replace("j", ":")
	s = s.replace("-", "")
	s = s.replace(" ", "")

	if s == "500":
		s = "Unknown"
	elif "d" in s:
		s = "Unknown"
	elif "a" in s:
		s = "Unknown"
	elif "p" in s:
		s = "Unknown"
	elif "n" in s:
		s = "Unknown"
	elif "x" in s:
		s = "Unknown"
	elif s == "":
		s = "Unknown"
	elif len(s) == 4:
		s= "Unknown"
	elif len(s) < 4:
		s = "Unknown"

	elif len(s) > 5:
		s = "Unknown"
	return s 


def clean_age(s):


	s = str(s)
	s = s.lower()

	s = s.replace("s", "")
	s = s.replace("'", "")
	
	if "teen" in s:
		s = "Unknown"
	elif "or" in s:
		s = "Unknown"
	elif "&" in s:
		s = "Unknown"
	elif ">" in s:
		s = "Unknown"
	elif "?" in s:
		s = "Unknown"
	elif "elderly" in s:
		s = "Unknown"
	elif "mid" in s:
		s = "Unknown"
	elif "adult" in s:
		s = "Unknown"
	elif "x" in s:
		s = "Unknown"
	elif "make" in s:
		s = "Unknown"
	elif "f" in s:
		s = "Unknown"
	elif "both" in s:
		s = "Unknown"
	elif "a.m." in s:
		s = "Unknown"
	elif "m" in s:
		s = "Unknown"
	elif "†" in s:
		s = "Unknown"
	elif "Ω" in s:
		s = "Unknown"
	elif "ω" in s:
		s = "Unknown"
	elif "month" in s:
		s = "1"
	elif "to" in s:
		s = "Unknown"
	elif "ca" in s:
		s = "Unknown"
	elif "nan" in s:
		s = "Unknown"
	elif "'young'" in s:
		s = "Unknown"
	elif "young" in s:
		s = "Unknown"

	s = s.replace(" ", "")
	if s == "":
		s = "Unknown"

	return s












def clean_empty_values(s):
	"""Esta función nos ayuda a convertir una columna en string y a quitarle los empty values."""

	s = str(s)

	if s == "Nan":
		s = "Not Available"

	elif s == "nan":
		s = "Not Available"

	elif s == "NaT":
		s = "Not Available"

	elif s == "Nat":
		s = "Not Available"

	elif s == "nat":
		s = "Not Available"

	return s 


def clean_country(s):
	"""Esta función nos ayudará a limpiar la lista de los países"""
	s = str(s)
	s = s. replace('/', '')
	s = s.replace('?', '')
	s = s.replace('REUNION', 'FRANCE')
	s = s.replace('Fiji', 'FIJI')
	s = s.replace('nan', 'Not Available')
	s = s.replace('(UAE)', '')
	s = s.replace('DIEGO GARCIA', 'Not Available')
	s = s.replace('Between PORTUGAL & INDIA', 'PORTUGAL-INDIA')
	s = s.replace('EGYPT / ISRAEL', 'EGYPT-ISRAEL')
	s = s.replace('EGYPT / ISRAEL', 'EGYPT-ISRAEL')
	s = s.replace('ANDAMAN / NICOBAR ISLANDAS', 'NICOBAR ISLANDS')
	s = s.replace('Sierra Leone', 'SIERRA LEONE')
	s = s.replace('St Helena', 'ENGLAND')
	s = s.replace('TURKS & CAICOS', 'TURKEY')
	s = s.replace('UNITED ARAB EMIRATES ()', 'UNITED ARAB EMIRATES')
	s = s.replace('Seychelles', 'SEYCHELLES')
	s = s.replace('CEYLON (SRI LANKA)', 'SRI LANKA')
	s = s.replace('WESTERN SAMOA', 'SAMOA')

	if "SEA" in s:
		s = "Not Available"
	elif "GULF" in s:
		s = "Not Available"
	elif "OCEAN" in s:
		s = "Not Available"

	return s


def clean_sex(s):


	if s == 'M ':
		s = 'M'
	elif s == 'lli':
		s = "Unidentified"
	elif s == 'N':
		s = 'M'
	elif s == '.':
		s == 'Unidentified'

	return s 


def clean_activity(s):
	s = str(s)
	s = s.lower()
	
	if "play" in s:
		s = "Playing"
	elif "surf" in s:
		s = "Surfing"
	elif "kayak" in s:
		s = "Kayaking"
	elif "float" in s:
		s = "Swimming"
	elif "windsurf" in s:
		s = "Windsurfing"
	elif "board" in s:
		s = "Boarding"
	elif "snorkel" in s:
		s = "Snorkeling"
	elif "spearfish" in s:
		s = "Spearfishing"
	elif "stand" in s:
		s = "Standing nearby"
	elif "div" in s:
		s = "Diving"
	elif "feed" in s:
		s = "Feeding fish or shark"
	elif "walk" in s:
		s = "Walking"
	elif "bath" in s:
		s = "Bathing"
	elif "watch" in s:
		s = "Standing nearby"
	elif "row" in s:
		s = "Rowing"
	elif "sit" in s:
		s = "Sitting"
	elif "splash" in s:
		s = "Splashing around"
	elif "sleep" in s:
		s = "Sleeping nearby"
	elif "freediv" in s:
		s = "Fre Diving"
	elif "film" in s:
		s = "Filming nearby"
	elif "ski" in s:
		s = "Water Skiing"
	elif "hunt" in s:
		s = "Hunting shark or other fish"
	elif "photograph" in s:
		s = "Taking pictures"
	elif "fish" in s:
		s = "Fishing"
	elif "sea disaster" in s:
		s = "Boat Accident"
	elif "boat" in s:
		s = "Boat Accident"
	elif "air disaster" in s:
		s = "Aircraft accident"
	elif "tread" in s:
		s = "Treading water"
	elif "paddle" in s:
		s = "Boarding"
	elif "boogie" in s:
		s = "Boarding"
	elif "body" in s:
		s = "Boarding"
	else:
		s = "Other"

	return s 

def clean_reference(s):
	"""This function will allow us to clean the two reference columns.""" 
	s = str(s)
	s = s.replace('∫', '')
	s = s.replace('‡', '')
	s = s.replace('?', '')
	s = s.replace('¯', '')
	s = s.replace('/', '')

	return s

#def clean_shark(s):
	"""This function will allow us to clean the Species column."""


def clean_injury(s):
	"""This function will help me categorize the different degrees of injuries."""
	s = str(s)
	s = s.lower()

	if s.startswith("no"):
		s = "0"
	elif "hoax" in s:
		s = "0"
	elif "erroneously" in s:
		s = "0"
	elif "stingray" in s:
		s = "0"

	elif "survived" in s:
		s = "0"
	elif "rescue" in s:
		s = "0"
	elif "harass" in s:
		s = "0"

	elif "minor" in s:
		s = "1"
	elif "laceration" in s:
		s = "1"
	elif "injury" in s:
		s = "1"
	elif "cut" in s:
		s = "1"
	elif "bite" in s:
		s = "1"
	elif "injuries" in s:
		s = "1"
	elif "fingers" in s:
		s = "1"
	elif "thigh" in s:
		s = "1"
	elif "superficial" in s:
		s = "1"
	elif "shin" in s:
		s = "1"
	elif "forearm" in s:
		s = "1"
	elif "small" in s:
		s = "1"
	elif "bruised" in s:
		s = "1"
	elif "cut" in s:
		s = "1"
	elif "lower" in s:
		s = "1"
	elif "upper" in s:
		s = "1"
	elif "neck" in s:
		s = "1"
	elif "head" in s:
		s = "1"
	elif "shoulders" in s:
		s = "1"
	elif "knee" in s:
		s = "1"
	elif "graze" in s:
		s = "1"
	elif "buttock" in s:
		s = "1"
	elif "severe" in s:
		s = "1"
	elif "amputated" in s:
		s = "1"
	elif "removed" in s:
		s = "1"
	elif "calf" in s:
		s = "1"
	elif "arm" in s:
		s = "1"
	elif "toe" in s:
		s = "1"
	elif "leg" in s:
		s = "1"
	elif "ankle" in s:
		s = "1"
	elif "puncture" in s:
		s = "1"
	elif "bit" in s:
		s = "1"
	elif "wrist" in s:
		s = "1"
	elif "bruise" in s:
		s = "1"
	elif "chest" in s:
		s = "1"
	elif "lacerat" in s:
		s = "1"
	elif "foot" in s:
		s = "1"
	elif "gash" in s:
		s = "1"
	elif "abrasion" in s:
		s = "1"
	elif "torn" in s:
		s = "1"
	elif "broken" in s:
		s = "1"
	elif "contusion" in s:
		s = "1"
	elif "injured" in s:
		s = "1"
	elif "hand" in s:
		s = "1"
	elif "struck" in s:
		s = "1"

	elif "face" in s:
		s = "1"
	elif "damage" in s:
		s = "1"
	elif "hurt" in s:
		s = "1"




	elif "taken" in s:
		s = "2"
	elif "remains" in s:
		s = "2"
	elif "perish" in s:
		s = "2" 
	elif "death" in s:
		s = "2"
	elif "dead" in s:
		s = "2"
	elif "fatal" in s:
		s = "2"
	elif "missing" in s:
		s = "2"
	elif "not recovered" in s:
		s = "2"
	elif "kill" in s:
		s = "2"
	elif "drown" in s:
		s = "2"
	elif "scavenge" in s:
		s = "2"
	
	else: 
		s = "Unregistered"

	return s











