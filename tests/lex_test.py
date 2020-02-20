import sys, unittest
sys.path.append(".")

from blzparser.lexer import BlitzLex
from blzparser.helper import helper

helper.no_out()

class TestBlitzLexer(unittest.TestCase):

    def test_segment1(self):
        prog = """
        var apples = 2;
        var oranges bl  = 3;
        var fruits = apples + oranges;
        out fruits;
        """

        lex = list(BlitzLex.segment(prog))
        ans = ['var', 'apples', '=', '2', ';', 'var', 'oranges', '=', '3', ';', 'var', 'fruits', '=', 'apples', '+', 'oranges', ';', 'out', 'fruits', ';']

        self.assertEqual(lex, ans)

    def test_segment2(self):
        prog = """
            func get_apples() {
                var apples = 2;
                return apples;
            };
        """

        lex = list(BlitzLex.segment(prog))
        ans = ['func', 'get_apples', '(', ')', '{', 'var', 'apples', '=', '2', ';', 'return', 'apples', ';', '}', ';']

        self.assertEqual(lex, ans)

    def test_segment_type(self):
        with self.assertRaises(TypeError):
            BlitzLex.segment(0).__next__()
        with self.assertRaises(TypeError):
            BlitzLex.segment(['list']).__next__()

    def test_tokenizer(self):
        prog = ['func', 'get_apples', '(', ')', '{', 'var', 'apples', '=', '2', ';', 'return', 'apples', ';', '}', ';']

        lex = list(BlitzLex.tokenizer(prog))
        ans = [('builtin', 'func'), ('variable', 'get_apples'), ('descriptor', '('), ('descriptor', ')'), ('descriptor', '{'), ('builtin', 'var'), ('variable', 'apples'), ('operator', '='),('number', '2'), ('descriptor', ';'), ('builtin', 'return'), ('variable', 'apples'), ('descriptor', ';'), ('descriptor', '}'), ('descriptor', ';')]

        self.assertEqual(lex, ans)

    def test_work(self):
        prog = """
            func get_apples() {
                var apples = 2;
                return apples;
            };
        """

        lex = list(BlitzLex.work(prog))
        ans = [('builtin', 'func'), ('variable', 'get_apples'), ('descriptor', '('), ('descriptor', ')'), ('descriptor', '{'), ('builtin', 'var'), ('variable', 'apples'), ('operator', '='),('number', '2'), ('descriptor', ';'), ('builtin', 'return'), ('variable', 'apples'), ('descriptor', ';'), ('descriptor', '}'), ('descriptor', ';')]

        self.assertEqual(lex, ans)

class TestBlitzParser(unittest.TestCase):
    def test_parse_tree(self):
        prog = [('builtin', 'func'), ('variable', 'get_apples'), ('descriptor', '('), ('descriptor', ')'), ('descriptor', '{'), ('builtin', 'var'), ('variable', 'apples'), ('operator', '='),('number', '2'), ('descriptor', ';'), ('builtin', 'return'), ('variable', 'apples'), ('descriptor', ';'), ('descriptor', '}'), ('descriptor', ';')]

        if prog:
            pass


