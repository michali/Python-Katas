'''
Created on 4 Nov 2012

@author: Michali
'''
import unittest
from NodeParser import NodeParser

class NodeParserTests(unittest.TestCase):

    def setUp(self):
        self.parser = NodeParser()

    def test_parses_a_plus(self):
        tree = self.parser.parse("1+2")
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(3, tree.evaluate())
        
    def test_parses_a_minus(self):
        tree = self.parser.parse("1-2")
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(-1, tree.evaluate())

    def test_parses_a_multiplication(self):
        tree = self.parser.parse("2*3")
        
        self.assertEqual(2, tree.left.evaluate())
        self.assertEqual(3, tree.right.evaluate())
        self.assertEqual(6, tree.evaluate())   
        
    def test_parses_a_division(self):
        tree = self.parser.parse("1/2")
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(0.5, tree.evaluate())     
        
    def test_parses_complex_no_brackets(self):
        tree = self.parser.parse("1+2/8")
               
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.left.evaluate())
        self.assertEqual(8, tree.right.right.evaluate())
        self.assertEqual(1.25, tree.evaluate())    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()