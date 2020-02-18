import os, sys, re
from blzparser.helper import helper

blitz_builtins = ['func', 'var', 'run', 'operate', 'return']
allowed_expr = "^[a-zA-Z0-9_]+$"
descriptors = "()[]{};\""

class BlitzLex:
    def __init__(self, file):
        pass

    @staticmethod
    def segment(file):
        if type(file) != str:
            helper._raise(TypeError("Must load a valid file!"))

        file = file.replace("\n", "")
        parts = []

        index = 0

        # seperate everything into tokens
        while index < len(file):
            c = 1

            # if it's just a space, ignore it
            if file[index] == " ":
                index += c
                continue

            # if it is among the syntax, append it
            elif file[index] in descriptors:
                parts.append(file[index])

            # else it is a name of a sort,
            # thus figure out how long this goes on
            # and when it is no longer a name, append it
            elif re.match(allowed_expr, file[index]):
                while re.match(allowed_expr, file[index:index+c]) and index+c <= len(file):
                    c += 1
                c -= 1
                parts.append(file[index:index+c])
            index += c
        
        
        return parts

    @staticmethod
    def tokenizer(tokens):
        if type(tokens) not in (list, tuple):
            helper._raise(TypeError("Cannot tokenize non-list-like"))

        determined = []
        for c, token in enumerate(tokens):
            if token in blitz_builtins:
                determined.append(('builtin', token))
            elif token in descriptors:
                determined.append(('descriptor', token))
            elif re.match("^[0-9.]+$", token):
                determined.append(('number', token))
            elif re.match("^[a-zA-Z0-9_]+$", token):
                determined.append(('variable', token))
            else:
                helper._raise(ValueError("Found unrecognizable token!"))
        return determined
