#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uuid

from xml.parsers import expat
from defusedxml.ElementTree import parse as ParseXML, XMLParser, ParseError
from xml.etree.ElementTree import Element, ElementTree

from .structures import MemoryFile


def ForgivingParse(data, entities=None) -> ElementTree:
    try:
        return ParseXML(MemoryFile(data), parser=ForgivingXMLParser(entities))
    except ParseError as PE:
        raise ValueError from PE


class ForgivingXMLParser(XMLParser):

    def __init__(self, emap=None):
        class ForgivingEntityResolver(dict):
            def __getitem__(self, key):
                if key in self:
                    return dict.__getitem__(self, key)
                uid = str(uuid.uuid4())
                self[key] = uid
                if emap is not None:
                    emap[uid] = key
                return uid

        self.__entity = ForgivingEntityResolver()
        _ParserCreate = expat.ParserCreate

        try:
            def PC(encoding, _):
                parser = _ParserCreate(
                    encoding, namespace_separator=None)
                parser.UseForeignDTD(True)
                return parser
            expat.ParserCreate = PC
            super().__init__()
        finally:
            expat.ParserCreate = _ParserCreate

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        self.__entity.update(value)


class XMLNodeCollection(list):
    def __getattr__(self, tag):
        result = self.__class__()
        for node in self:
            for child in node.children:
                if child.tag != tag:
                    continue
                result.append(child)
        return result


class XMLNode:
    __slots__ = 'tag', 'children', 'attributes', 'content', 'parent'

    def __init__(self, tag: str):
        self.tag: str = tag
        self.children = []
        self.attributes = {}
        self.content = None
        self.parent = None

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, key):
        return self.attributes[key]

    def get_attribute(self, key, default=None):
        return self.attributes.get(key, default)

    @property
    def subtree(self):
        return XMLNodeCollection((self,))

    def __enter__(self):
        return self.subtree

    def __exit__(self, *a):
        return False


def parse(data) -> XMLNode:
    def translate(element: Element, cursor: XMLNode, level: int = 0):
        for child in element:
            node = XMLNode(child.tag)
            translate(child, node, level + 1)
            node.parent = cursor
            cursor.children.append(node)
        cursor.attributes = element.attrib
        cursor.content = element.text or element.tail or ''
        return cursor
    root = ForgivingParse(data).getroot()
    return translate(root, XMLNode(root.tag))