"""
Treatment function module
"""
import sys
import re
import itertools
import os
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

    # Opening in add mode
    with open(path_input + '.lama', "a") as list_pers:
        #  while user have data to record
        while True:
            #  Creating a temporary list to store inputs.
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

            #  Adding input in the file
            for i, elt in enumerate(temp_list):
                list_pers.write(elt + "\n")

            #  Deleting the temporary list
            del temp_list


def leet(chaine):
    """Leet Function:
        Input : string
        Output: string"""
    dico_leet = {"a": "4", "e": "3", "i": "1", "s": "5", "t": "7", "b": "8", "o": "0"}
    chaine = chaine.lower()

    for i, elt in dico_leet.items():
        chaine = chaine.replace(i, elt)

    return chaine


def write_all_perm(Alist, Afile, Alen):
    """Permutation Function:
    Input: list, namefile, int, boolean
    Output: file
    """
    x = 2
    while x <= len(Alist):
        for perm in list(itertools.permutations(Alist, x)):
            chain = ""
            y = x - 1
            while y >= 0:
                chain = chain + perm[y]
                y -= 1
                if len(chain) <= Alen:
                    Afile.write(chain + "\n")
    x += 1


def Lama(list_raw, output, mlen, l33t):
    """Password Function
    Input : List, Filename,
    Output: .lama"""

    #  Removing the "\n"
    for i, elt in enumerate(list_raw):
        list_raw[i] = list_raw[i][:len(list_raw[i]) - 1]

    #  If there is an error about the size of the list.
    try:
        #  Separating day from month from year.
        list_nb_date = [list_raw[2][:2], list_raw[2][3:5], list_raw[2][6:], list_raw[2][8:]]
        #  Putting postal code and short postal code in a separated list.
        list_cp = [list_raw[4], list_raw[4][:2]]
        #  Putting Name and surname in a separated list.
        list_name = [list_raw[0], list_raw[1]]
    except IndexError:
        print """the Input list isn't complete (missing line):
        ==>> Running operation aborted! <<=="""
        sys.exit(0)

    #  TODO : improve the quality of the wordlist by creating better lists.
    # Here there is some "useless permutation"

    list_name.extend(list_nb_date)
    list_name.extend(list_cp)

    with open(output + '.lama', "a") as wordlist:
        write_all_perm(list_name, wordlist, mlen)

    Mo = os.path.getsize('./{0}.lama'.format(output)) / 1048576
    print "A Lama-wordlist {0}.lama was successfully created ({1} Mo)".format(output, Mo)
