import sys, unittest
sys.path.append(".")

from blzparser.lexer import BlitzLex

class TestBlitzLexer(unittest.TestCase):
    def test_simple(self):
        prog = """
            func get_apples() {
                var applees = 2;
                return apples;
            };
        """

        lex = BlitzLex.segment(prog)
        ans = ['func', 'get_apples', '(', ')', '{', 'var', 'applees', '2', ';', 'return', 'apples', ';', '}', ';']

        assert lex == ans



