"""Je suis le module de traitement"""

def traitement(surname,name,birthdate,hometown,postalcode,*empty):
	"""Je suis la fonction de traitement"""
	print("###Traitement###")
	day = birthdate[:2]
	month = birthdate[3:5]
	year = birthdate[6:]


	# ouverture en mode ajout.
	with open("output","a") as wordlist_mdp:
		#rules of password creations...
		wordlist_mdp.write(surname+name+month+day+"\n")
		wordlist_mdp.write(surname+day+"\n")