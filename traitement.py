"""Je suis le module des fonctions de traitement"""
import sys
import re
from itertools import chain, islice, permutations

def morceaux(iterable, taille, format=iter):
	"""DOC morceaux: Parcours d'iterable par morceaux"""
	it = iter(iterable)
	while True:
		yield format(chain((it.next(),), islice(it, taille - 1)))

def add_entry(path_input):
	"""Je suis la fonction d'ajout d'entrees manuelle"""
	# ouverture en mode ajout.
	d_ex = r"^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$"
	p_ex = r"^(0[1-9]|[1-9][0-9])[0-9]{3}$"

	with open(path_input,"a") as list_pers:
		
		while 1: #while user have data to record
			print ("Press enter now to stop")
			surname = raw_input("Surname []: ")

			if len(surname) == 0:
				break
			#TODO improve that
			try:
				name = raw_input("Name []: ")
				birthdate = raw_input("Birthdate dd/mm/yyyy []:")

				if re.match(d_ex, birthdate) == None:
				 	raise ValueError("Birth date format not match")

				hometown = raw_input("Hometown []:")
				postalcode = raw_input("Postalcode xxxxx []:")

				if re.match(p_ex, postalcode) == None:
				 	raise ValueError("Postalcode format not match")

			except TypeError:
				print("Something went wrong")


			list_pers.write(surname + "\n")
			list_pers.write(name + "\n")
			list_pers.write(birthdate + "\n")
			list_pers.write(hometown + "\n")
			list_pers.write(postalcode + "\n")

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
	"""Je suis la fonction de permutation de tout les elements de la liste"""
	if len(elements) <=1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				#nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]


def traitement(morceau, output):
	"""Je suis la fonction de traitement"""

	#Removing the "\n"
	for i, elt in enumerate(morceau):
		morceau[i] = morceau[i][:len(morceau[i])-1]

	print morceau

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
#TODO finish that or rethink it ... => write in a file
#TODO little permutation ?
#TODO ...
	print output
	with open(output, "a") as wordlist:
		for perm in all_perms(morceau):
			wordlist.write(perm[0]+perm[1]+perm[2]+"\n")
			wordlist.write(leet(perm[0]+perm[1]+perm[2])+"\n")