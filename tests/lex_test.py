import sys, unittest
sys.path.append(".")

from blzparser.lexer import BlitzLex
from blzparser.helper import helper

helper.no_out()

class TestBlitzLexer(unittest.TestCase):
    def test_simple(self):
        prog = """
            func get_apples() {
                var apples = 2;
                return apples;
            };
        """

        lex = BlitzLex.segment(prog)
        ans = ['func', 'get_apples', '(', ')', '{', 'var', 'apples', '2', ';', 'return', 'apples', ';', '}', ';']

        self.assertEqual(lex, ans)

    def test_type(self):
        with self.assertRaises(TypeError):
            BlitzLex.segment(0)
        with self.assertRaises(TypeError):
            BlitzLex.segment(['list'])

    def test_tokenizer(self):
        prog = ['func', 'get_apples', '(', ')', '{', 'var', 'apples', '2', ';', 'return', 'apples', ';', '}', ';']

        lex = BlitzLex.tokenizer(prog)
        ans = [('builtin', 'func'), ('variable', 'get_apples'), ('descriptor', '('), ('descriptor', ')'), ('descriptor', '{'), ('builtin', 'var'), ('variable', 'apples'), ('number', '2'), ('descriptor', ';'), ('builtin', 'return'), ('variable', 'apples'), ('descriptor', ';'), ('descriptor', '}'), ('descriptor', ';')]

        self.assertEqual(lex, ans)





