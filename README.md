LAMA-WORDLIST
===========

Introduction To The Project
=======================

The project Lama-wordlist is made to gather informations on social networks and create intelligent word-lists with these informations. 
The informations gathered on social networks will be focus on a person who will be the target of futur brute-forcing attack.

Gathering
---------
Informations gathered about the target will be as follow:
	-first-name.
	-last-name.
	-birth-date.
	-home-town.
	-friends:
		-first-name.
		-last-name.
		-birth-date.
		-home-town.

Formating 
---------
These informations will be stored in a file under an appropriate format/structures.

Generation
---------
The wordlist will be created with a mix of all the informations based on research on common passwords.
Most of the passwords is created with a name of relatives plus a date behind or after the name.
So Lama-wordlist will create this permutations with the date the name and the postal code.

Example:
Info gathered: Martin Foo 12/02/1950 Metz
Martinfoo
MartinFoo
Martin1950
Foo1950
Martin57
Foo57
M4rt1n57
F001950
Martin1202
1202Martin
12Martin1950
etc...
