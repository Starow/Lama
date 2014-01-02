"""Je suis le module des fonctions de traitement"""
from itertools import chain, islice

def morceaux(iterable, taille, format=iter):
	"""DOC morceaux: Parcours d'iterable par morceaux"""
	it = iter(iterable)
	while True:
		yield format(chain((it.next(),), islice(it, taille - 1)))

def leet(chaine):
	"""Je suis la fonction de transformation en alphabet leet"""
	dico_leet = { "a":"4", "e":"3", "i":"1", "s":"5", "t":"7", "b":"8", "o":"0" }
	chaine = chaine.lower()

	for cle, val in dico_leet.items():
		chaine = chaine.replace(cle,val)

	return chaine

def traitement(surname,name,birthdate,hometown,postalcode,output,*empty):
	"""Je suis la fonction de traitement"""
	day = birthdate[:2]
	month = birthdate[3:5]
	year = birthdate[6:]
	short_post = postalcode[:2]

	# ouverture en mode ajout.
	with open(output,"a") as wordlist:
		#rules of password creations...
		# TODO find a permutation algorithm for this job

		wordlist.write(surname + "\n")
		wordlist.write(name + "\n")
		wordlist.write(surname + name + "\n")
		wordlist.write(name + surname + "\n")

		wordlist.write(day + surname + "\n")
		wordlist.write(day + name + "\n")
		wordlist.write(day + surname + name + "\n")
		wordlist.write(day + name + surname + "\n")

		wordlist.write(surname + day + "\n")
		wordlist.write(name + day + "\n")
		wordlist.write(surname + name + day + "\n")
		wordlist.write(name + surname + day + "\n")

		wordlist.write(surname + year + "\n")
		wordlist.write(name + year + "\n")
		wordlist.write(surname + name + year + "\n")
		wordlist.write(name + surname + year + "\n")

		wordlist.write(year + surname + "\n")
		wordlist.write(year + name + "\n")
		wordlist.write(year + surname + name + "\n")
		wordlist.write(year + name + surname + "\n")

		wordlist.write(surname + short_post + "\n")
		wordlist.write(name + short_post + "\n")
		wordlist.write(surname + name + short_post + "\n")
		wordlist.write(name + surname + short_post + "\n")

		wordlist.write(short_post + surname + "\n")
		wordlist.write(short_post + name + "\n")
		wordlist.write(short_post + surname + name + "\n")
		wordlist.write(short_post + name + surname + "\n")

		#leet one
		wordlist.write(leet(surname) + "\n")
		wordlist.write(leet(name) + "\n")
		wordlist.write(leet(surname + name) + "\n")
		wordlist.write(leet(name + surname) + "\n")


		
		