import os, sys
from blzparser.helper import *
from blzparser.lexer import BlitzLex

def _find_closure(s, start, end):
    n = 0
    for ch in s:
        if ch == end and n == 0:
            return n
        elif ch == end:
            n += 1
        elif ch == start:
            n -= 1
    return False

def _find_next(s, seg):
    for c, _ in enumerate(s):
        if s[c:c+len(seg)] == seg:
            return c
    return False

class BlitzParse:
    INFO = []
    WARNING = []
    ERROR = []

    def __init__(self):
        pass

    def parse(self, file):
        pass



def main():

    if len(sys.argv) < 2:
        helper.out("File not specified!", level = 2)
    


if __name__ == '__main__':
    main()



