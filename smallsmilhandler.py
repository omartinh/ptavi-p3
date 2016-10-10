#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.lista = []

    def startElement(self, name, attrs):

        if name == "root-layout":
            self.root_layout = {}
            self.lista.append(name)
            self.root_layout['width'] = attrs.get('width', "")
            self.root_layout['height'] = attrs.get('height', "")
            self.root_layout['background-color'] = attrs.get('background-color', "")
            self.lista.append(self.root_layout)

        elif name == 'region':
            self.region = {}
            self.lista.append(name)
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            self.lista.append(self.region)

        elif name == 'img':

            self.img = {}
            self.lista.append(name)
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            self.lista.append(self.img)

        elif name == 'audio':

            self.audio = {}
            self.lista.append(name)
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")
            self.lista.append(self.audio)

        elif name == 'textstream':

            self.textstream = {}
            self.lista.append(name)
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.lista.append(self.textstream)

    def get_tags(self):
        return self.lista


def imprimir_list(lista):
    for linea in lista:
        print(linea)

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))

    imprimir_list(cHandler.get_tags())
