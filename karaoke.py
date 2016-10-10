#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

import sys
import json
import urllib



def print_lista(lista):
    for linea in lista:
        atrib = ""
        if isinstance(linea, dict):
            for elem in linea:
                atrib = atrib + elem + "=" + linea[elem] + "\t"
            print(etiq + "\t" + atrib)
        else:
            etiq = linea

def URL_finder(lista):

    URL_l = []

    for linea in lista:
        if isinstance(linea, dict):
            for elem in linea:
                if elem == "src":
                   URL_l.append(linea[elem])
    return URL_l
 

def URL_files(u_l):

    for linea in u_l:
        f_l = linea.split("/")
        url_file = f_l[-1]
        try:
            urllib.request.urlretrieve(linea, url_file)
        except ValueError:
            sys.exit("Not URL file")

if __name__ == "__main__":

    try:
        fich = sys.argv[1]
    except:
        sys.exit("Usage: Python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fich))
    lista = SmallSMILHandler.get_tags(cHandler)

    print_lista(lista)

    URL_list = URL_finder(lista)
    URL_files(URL_list)
    
    fich_json = open('karaoke.json', 'w')
    json.dump(lista, fich_json, sort_keys=True, indent=4, separators=(',', ':'))
    fich_json.close()
