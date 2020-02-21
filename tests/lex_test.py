import sys, unittest
sys.path.append(".")

from blzparser.lexer import BlitzLex
from blzparser.helper import helper as hlp

hlp.no_out()

class TestBlitzLexer(unittest.TestCase):

    def test_segment1(self):
        prog = """
        var apples = 2;
        var oranges = 3;
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
        ans = [(hlp.BUILTIN, 'func'), (hlp.VARIABLE, 'get_apples'), (hlp.DESCRIPTOR, '('), (hlp.DESCRIPTOR, ')'), (hlp.DESCRIPTOR, '{'), (hlp.BUILTIN, 'var'), (hlp.VARIABLE, 'apples'), (hlp.OPERATOR, '='),(hlp.NUMBER, '2'), (hlp.DESCRIPTOR, ';'), (hlp.BUILTIN, 'return'), (hlp.VARIABLE, 'apples'), (hlp.DESCRIPTOR, ';'), (hlp.DESCRIPTOR, '}'), (hlp.DESCRIPTOR, ';')]

        self.assertEqual(lex, ans)

    def test_work(self):
        prog = """
            func get_apples() {
                var apples = 2;
                return apples;
            };
        """

        lex = list(BlitzLex.work(prog))
        ans = [(hlp.BUILTIN, 'func'), (hlp.VARIABLE, 'get_apples'), (hlp.DESCRIPTOR, '('), (hlp.DESCRIPTOR, ')'), (hlp.DESCRIPTOR, '{'), (hlp.BUILTIN, 'var'), (hlp.VARIABLE, 'apples'), (hlp.OPERATOR, '='),(hlp.NUMBER, '2'), (hlp.DESCRIPTOR, ';'), (hlp.BUILTIN, 'return'), (hlp.VARIABLE, 'apples'), (hlp.DESCRIPTOR, ';'), (hlp.DESCRIPTOR, '}'), (hlp.DESCRIPTOR, ';')]

        self.assertEqual(lex, ans)

class TestBlitzParser(unittest.TestCase):
    def test_parse_tree(self):
        prog = [(hlp.BUILTIN, 'func'), (hlp.VARIABLE, 'get_apples'), (hlp.DESCRIPTOR, '('), (hlp.DESCRIPTOR, ')'), (hlp.DESCRIPTOR, '{'), (hlp.BUILTIN, 'var'), (hlp.VARIABLE, 'apples'), (hlp.OPERATOR, '='),(hlp.NUMBER, '2'), (hlp.DESCRIPTOR, ';'), (hlp.BUILTIN, 'return'), (hlp.VARIABLE, 'apples'), (hlp.DESCRIPTOR, ';'), (hlp.DESCRIPTOR, '}'), (hlp.DESCRIPTOR, ';')]

        if prog:
            pass


