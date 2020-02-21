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

class Operation(object):
    def __init__(self, *args, **kwargs):
        pass

    def evl(self):
        return 0


class PLUS(Operation):
    @staticmethod
    def evl(obj1, obj2):
        return obj1 + obj2


class MINUS(Operation):
    @staticmethod
    def evl(obj1, obj2):
        return obj1 - obj2


class MULT(Operation):
    @staticmethod
    def evl(obj1, obj2):
        return obj1 * obj2


class DIV(Operation):
    @staticmethod
    def evl(obj1, obj2):
        return obj1 / obj2


class ASSIGN(Operation):
    def __init__(self, name, value):
        self.name, self.value = name, value

    def evl(self):
        return self.value

class Node(object):
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

    def evl(self):
        return self.op.evl(self.left, self.right)


class BlitzParse:

    def __init__(self):
        pass

    def parse(self, tokens):
        flags = {
        'setting-name'  :0,
        'defining-func' :0,
        'enclosement'   :0,
        }

        for typ, nam in tokens:
            pass




def main():

    if len(sys.argv) < 2:
        helper.out("File not specified!", level = 2)



if __name__ == '__main__':
    main()



