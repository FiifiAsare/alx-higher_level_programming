#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.remove(key=" ")
    if a_dictionary.remove(key=" ") != 1:
         return a_dictionary
