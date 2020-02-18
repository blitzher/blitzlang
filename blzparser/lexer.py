import os
import sys
import re

blitz_builtins = ['func', 'var', 'run', 'operate', 'return']
allowed_expr = "^[a-zA-Z0-9_]+$"
descriptors = "()[]{};\""

class BlitzLex:
    def __init__(self, file):
        pass

    @staticmethod
    def segment(file):
        assert type(file) == str
        file = file.replace("\n", "")

        parts = []

        index = 0
        while index < len(file):
            c = 1
            if file[index] == " ":
                index += c
                continue
            elif file[index] in descriptors:
                parts.append(file[index])
            elif re.match(allowed_expr, file[index]):
                while re.match(allowed_expr, file[index:index+c]):
                    c += 1
                c -= 1
                parts.append(file[index:index+c])
            index += c
        return parts


