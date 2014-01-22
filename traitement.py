"""Je suis le module des fonctions de traitement"""
import sys
import re
from itertools import chain, islice, permutations

def Windowing(iterable, taille, format=iter):
	"""Windowing Function"""
	it = iter(iterable)
	while True:
		yield format(chain((it.next(),), islice(it, taille - 1)))

def add_entry(path_input):
	"""Adding Entry Function
	Input : Filename
	Output: .lama"""
	
	d_ex = r"^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$"
	p_ex = r"^(0[1-9]|[1-9][0-9])[0-9]{3}$"

	# Ouverture en mode ajout.
	with open(path_input+'.lama',"a") as list_pers:
		
		#while user have data to record
		while True: 
			#Creating a temporary list to store inputs.
			temp_list = []

			print "Press enter now to stop"
			temp_list.append(raw_input("Surname []: "))

			if len(temp_list[0]) == 0:
				break

			temp_list.append(raw_input("Name []: "))

			while True:
				temp_list.append(raw_input("Birthdate dd/mm/yyyy []:"))
				if re.match(d_ex, temp_list[2]) is not None:
					break
				print "Birthdate Format is not correct"

			temp_list.append(raw_input("Hometown []:"))

			while True:
				temp_list.append(raw_input("Postalcode xxxxx []:"))
				if re.match(p_ex, temp_list[4]) is not None:
					break
				print "Postalcode Format is not correct"

			#Adding input in the file
			for i, elt in enumerate(temp_list):
				list_pers.write(elt + "\n")

			#Deleting the temporary list
			del temp_list;

def leet(chaine):
	"""Leet Function:
	Input : string
	Output: string"""
	dico_leet = { "a":"4", "e":"3", "i":"1", "s":"5", "t":"7", "b":"8", "o":"0" }
	chaine = chaine.lower()

	for i, elt in dico_leet.items():
		chaine = chaine.replace(i,elt)

	return chaine


def all_perms(elements):
	"""Permutation Function
	Input : String or list
	Output: String or list"""
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				#nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]


def Lama(morceau, output):
	"""Password Function
	Input : List, Filename,
	Output: .lama"""

	#Removing the "\n"
	for i, elt in enumerate(morceau):
		morceau[i] = morceau[i][:len(morceau[i])-1]

	#Separating day from month from year
	list_nb_date = [morceau[2][:2],morceau[2][3:5],morceau[2][6:],morceau[2][8:]]
	#Putting postal code and short postal code in a separated list
	list_cp = [morceau[4],morceau[4][:2]]
	#Deleting raw date format
	del morceau[2]
	#Deleting the name of the city *** Dunno what to do with it
	del morceau[2]
	#Concat date to morceau
	#morceau.extend(date)
	# short_post = postalcode[:2]
	print morceau
	print list_nb_date
	print list_cp


#Uncomplete
#TODO little permutation...
#TODO Create intelligent little list to permutate.
	with open(output+'.lama', "a") as wordlist:
		for perm in all_perms(morceau):
			wordlist.write(perm[0]+perm[1]+perm[2]+"\n")
			#wordlist.write(leet(perm[0]+perm[1]+perm[2])+"\n")