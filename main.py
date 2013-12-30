#!/usr/bin/python2.7
# -*-coding:UTF-8 -*

import string
from traitement import *
from itertools import chain, islice

def morceaux(iterable, taille, format=iter):
	"""DOC morceaux: Parcours d'iterable par morceaux"""
	it = iter(iterable)
	while True:
		yield format(chain((it.next(),), islice(it, taille - 1)))

#with pour eviter les prob d'ouverture et fermeture.
with open("fichier","r") as list_pers:
	for morceau in morceaux(list_pers, 5, tuple):
		#traitement ...
		traitement(morceau[0][:len(morceau[0])-1],morceau[1][:len(morceau[1])-1],morceau[2][:len(morceau[2])-1],morceau[3][:len(morceau[3])-1],morceau[4][:len(morceau[4])-1])
		print morceau
