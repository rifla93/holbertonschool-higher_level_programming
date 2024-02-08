#!/usr/bin/python3
'''
json file
'''


def read_file(filename=""):
    '''
    json file
    '''

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
