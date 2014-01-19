#!/usr/bin/python2.7
# -*-coding:UTF-8 -*

import argparse
from traitement import *

def main():
	"""Main Function"""

	parser = argparse.ArgumentParser(description = 'Create passwords wordlist\
		.', epilog = 'Copyright: Staross & Benesaii // 2014')

	parser.add_argument('input', type = str, help = 'input file', action = 'store')
	parser.add_argument('output', type = str, help = 'output file', action = 'store')
	parser.add_argument('--add', help = 'add manual entries', action = 'store_true')
	args = parser.parse_args()

	if args.add == True:
		add_entry(args.input)

	#with pour les prob d'open/close.
	with open(args.input,"r") as list_pers:
		for morceau in Windowing(list_pers, 5, list):
			#traitement du fichier input...
			#TODO traitement de l'erreur si le fichier input est incomplet
			Lama(morceau, args.output)

if __name__ == "__main__":
    main()