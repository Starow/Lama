#!/usr/bin/python2.7
# -*-coding:UTF-8 -*

import argparse
from traitement import *

def main():
	"""Fonction main gamin"""

	parser = argparse.ArgumentParser(description = 'Create passwords wordlist.'\
		, epilog = 'Copyright: Staross & Benesaii // 2014')

	parser.add_argument('input', type = str, help = 'input file', action = 'store')
	parser.add_argument('output', type = str, help = 'output file', action = 'store')
	parser.add_argument('--add', help = 'add manual entries', action = 'store_true')
	args = parser.parse_args()

	if args.add == True:
		add_entry(args.input)

	#with pour les prob d'open/close.
	with open(args.input,"r") as list_pers:
		for morceau in morceaux(list_pers, 5, tuple):
			#traitement du fichier input...
			#TODO traitement de l'erreur si le fichier input est malformé (incomplet)
			traitement(morceau[0][:len(morceau[0])-1],\
				morceau[1][:len(morceau[1])-1],\
				morceau[2][:len(morceau[2])-1],\
				morceau[3][:len(morceau[3])-1],\
				morceau[4][:len(morceau[4])-1],\
				args.output)
			print morceau

if __name__ == "__main__":
    main()