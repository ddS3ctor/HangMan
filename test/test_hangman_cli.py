import sys
import unittest
import hangman_cli
from io import StringIO

class HangManCli(unittest.TestCase):
    def test_print_table_1_hidden(self):
        word = 'challenge'
        hidden = [5]
        output = StringIO()
        sys.stdout = output
        hangman_cli.print_table(word, hidden)
        compare = '''+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
+---+---+---+---+---+---+---+---+---+
| c | h | a | l | l | _ | n | g | e |
+---+---+---+---+---+---+---+---+---+
| score:  0 |
+-----------+
'''
        self.assertEqual(output.getvalue(), compare)


if __name__ == '__main__':
    unittest.main()