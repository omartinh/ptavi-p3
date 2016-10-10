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

    fich_json = open('karaoke.json', 'w')
    json.dump(lista, fich_json, sort_keys=True, indent=4, separators=(',',':'))
    fich_json.close()
