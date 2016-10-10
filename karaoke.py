#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

import sys
import json
import urllib


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fich):

        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fich))
        self.lista = SmallSMILHandler.get_tags(cHandler)

    def __str__(self):

        atrib = ""
        for linea in self.lista:
            if isinstance(linea, dict):
                for elem in linea:
                    atrib = atrib + elem + "=" + linea[elem] + "\t"
                atrib = atrib + "\n"
            else:
                atrib = atrib + linea + "\t"
        return(atrib)

    def to_json(self, fich, new_fich=""):
        if new_fich == "":
            nf = fich[:fich.find('.')]
        else:
            nf = new_fich
        fich_json = open(nf + '.json', 'w')
        json.dump(self.lista, fich_json, sort_keys=True, indent=4, separators=(',', ':'))
        fich_json.close()

    def do_local(self):
        for linea in self.lista:
            if isinstance(linea, dict):
                if 'src' in linea:
                    if linea['src'] != 'cancion.ogg':
                        local = linea['src'].split("/")[-1]
                        urllib.request.urlretrieve(linea['src'], local)


if __name__ == "__main__":

    try:
        fich = sys.argv[1]
    except:
        sys.exit("Usage: Python3 karaoke.py file.smil")

    try:
        karaoke = KaraokeLocal(fich)
    except FileNotFoundError:
        sys.exit("Error: File not found")

    print(karaoke)
    karaoke.to_json(fich)
    karaoke.do_local()
    karaoke.to_json(fich, 'local')
    print(karaoke)
