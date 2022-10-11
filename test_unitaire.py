from unittest import TestCase
import unittest
#import sys
#sys.path.append("..")
from factoriel import factoriel
class Testfactoriel(TestCase):
    def setUp(self):
        self.n = 3

    def testfactoriel(self):
        f3 = factoriel(self.n)
        self.assertEqual(6,f3)

if __name__=='__main__':
    unittest.main()