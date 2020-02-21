
class helper:
    """
    big class for handling all minor function calls and most constants

    handles all forms of communication with the command line, and output
    # TODO including logging


    """

    _out_level = 0

    BUILTIN     = 0
    VARIABLE    = 1
    DESCRIPTOR  = 2
    OPERATOR    = 3
    NUMBER      = 4



    @staticmethod
    def out(message, level = 0):
        if level < helper._out_level:
            return
        gravity = ['INFO', 'WARNING', 'ERROR'][level]
        print(f"[BZ {gravity}]: {message}")

    @staticmethod
    def _raise(err):
        helper.out(err, level=2)
        raise err

    @staticmethod
    def set_out_level(level):
        if level not in {0,1,2}:
            helper._raise(ValueError("Cannot set out level to number not between 0 and 2!"))
        helper._out_level = level

    @staticmethod
    def no_out():
        helper._out_level = 3
