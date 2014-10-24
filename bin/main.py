#!/usr/bin/python2.7
# -*-coding:UTF-8 -*

import argparse
from traitement import *

def main():
	"""Main Function"""

	parser = argparse.ArgumentParser(description = 'Create passwords wordlist.',
        epilog = 'Copyright: Staross & Benesaii // 2014')

	parser.add_argument('input',
        type = str,
        help = 'Input file name',
        action = 'store')

	parser.add_argument('output',
        type = str,
        help = 'Output file name',
        action = 'store')

	parser.add_argument('--add',
        help = 'Add manual entries',
        action = 'store_true')

	parser.add_argument('--l33t',
        help = 'Toggle the leet treatment',
        action = 'store_true')

	parser.add_argument('--mlen',
        default = 24,
        type = int,
        help = 'Define the max lenght of pass created (default = 24)',
        action = 'store')

	args = parser.parse_args()

	if args.add == True:
		add_entry(args.input)

	#with pour les prob d'open/close.
	with open(args.input+'.lama',"r") as list_pers:
		for morceau in Windowing(list_pers, 5, list):
			#traitement du fichier input...
			#TODO traitement de l'erreur si le fichier input est incomplet
			Lama(morceau, args.output, args.mlen, args.l33t)

if __name__ == "__main__":
    main()
