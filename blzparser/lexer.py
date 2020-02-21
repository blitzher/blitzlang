import os, sys, re
from blzparser.helper import helper as hlp

blitz_builtins = ['func', 'var', 'run', 'out', 'operate', 'return', 'if']
allowed_expr = "^[a-zA-Z0-9_]+$"
descriptors = "()[]{};\""
operators = r"^[=\+\-\*\/]=?$"

class BlitzLex:

    @staticmethod
    def segment(file):
        """ converts a str, looking like a .bz program
        to segments, following the blitz logic

        returns a generator yielding these segments

        BlitzLex.segment(str) -> <generator>
        """
        if type(file) != str:
            hlp._raise(TypeError("Must take a str as argument!"))

        file = file.replace("\n", " ")

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
                yield file[index]

            # else it is a name of a sort,
            # thus figure out how long this goes on
            # and when it is no longer a name, append it
            elif re.match(allowed_expr, file[index]):
                while re.match(allowed_expr, file[index:index+c]) and index+c <= len(file):
                    c += 1
                c -= 1
                yield file[index:index+c]

            # do the same for multichar operators
            elif re.match(operators, file[index]):
                while re.match(operators, file[index:index+c]) and index+c <= len(file):
                    c+= 1
                c -= 1
                yield file[index:index+c]
            index += c

    @staticmethod
    def token_one(token):
        if token in blitz_builtins:
            return (hlp.BUILTIN, token)
        elif token in descriptors:
            return (hlp.DESCRIPTOR, token)
        elif re.match("^[0-9.]+$", token):
            return (hlp.NUMBER, token)
        elif re.match("^[a-zA-Z0-9_]+$", token):
            return (hlp.VARIABLE, token)
        elif re.match(operators, token):
            return (hlp.OPERATOR, token)
        else:
            hlp._raise(ValueError("Found unrecognizable token!"))

    @staticmethod
    def tokenizer(segments):
        """converts segments to tokens """
        if type(segments) not in (list, tuple):
            hlp._raise(TypeError("Cannot tokenize non-list-like"))

        for token in segments:
            yield BlitzLex.token_one(token)


    @staticmethod
    def work(file):
        """combine the functionality of segment and tokenize in one"""
        for segment in BlitzLex.segment(file):
            yield BlitzLex.token_one(segment)

def main():
    pass

if __name__ == '__main__':
    main()