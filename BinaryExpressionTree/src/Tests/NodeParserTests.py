'''
Created on 4 Nov 2012

@author: Michali
'''
import unittest
from NodeParser import NodeParser
from mock import Mock

class NodeParserTests(unittest.TestCase):

    def setUp(self):
        self.mock = Mock()
        self.parser = NodeParser(self.mock)

    def test_parses_a_plus(self):
        exp = "1+2"
        self.mock.transform.return_value = "1 2 +"
        tree = self.parser.parse(exp)
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(3, tree.evaluate())
        
    def test_parses_a_minus(self):
        exp = "1-2"
        self.mock.transform.return_value = "1 2 -"
        tree = self.parser.parse(exp)
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(-1, tree.evaluate())

    def test_parses_a_multiplication(self):
        exp = "2*3"
        self.mock.transform.return_value = "2 3 *"
        tree = self.parser.parse(exp)
        
        self.assertEqual(2, tree.left.evaluate())
        self.assertEqual(3, tree.right.evaluate())
        self.assertEqual(6, tree.evaluate())   
        
    def test_parses_a_division(self):
        exp = "1/2"
        self.mock.transform.return_value = "1 2 /"
        tree = self.parser.parse(exp)
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(0.5, tree.evaluate())     
        
    def test_parses_complex_no_brackets(self):
        exp = "1+2/8"
        self.mock.transform.return_value = "1 2 8 / +"
        tree = self.parser.parse(exp)
           
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.left.evaluate())
        self.assertEqual(8, tree.right.right.evaluate())
        self.assertEqual(1.25, tree.evaluate())    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()