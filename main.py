#!/usr/bin/python2.7
# -*-coding:UTF-8 -*

from traitement import *

output_file_name = "output"
input_file_name = "input"
input_file_name = raw_input("Path to the input file: ")
output_file_name = raw_input("Path to the output file (created if not exist): ")

#with pour eviter les prob d'ouverture et fermeture.
with open(input_file_name,"r") as list_pers:
	for morceau in morceaux(list_pers, 5, tuple):
		#traitement ...
		traitement(morceau[0][:len(morceau[0])-1],morceau[1][:len(morceau[1])-1],morceau[2][:len(morceau[2])-1],morceau[3][:len(morceau[3])-1],morceau[4][:len(morceau[4])-1],output_file_name)
		print morceau