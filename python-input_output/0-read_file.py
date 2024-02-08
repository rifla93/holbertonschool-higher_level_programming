#!/usr/bin/python3
'''
json file

'''


import json


def read_file(filename=""):
    '''
    json file
    '''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
