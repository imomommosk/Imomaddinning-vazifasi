import unittest
from main import kattason
from main import text_list

class Sontest(unittest.TestCase):
    def sonmax(self):
        self.assertEqual(kattason(1, 3, 66))
        self.assertEqual(kattason(2, 5, 5))

    def tittle(self):
        self.assertEqual(text_list("jonibek"))

unittest.main()