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

    def parse_expression(self, exp, rpn_exp):
        self.mock.transform.return_value = rpn_exp
        tree = self.parser.parse(exp)
        return tree

    def test_parses_a_plus(self):
        tree = self.parse_expression("1+2", "1 2 +")
        
        self.mock.transform.assert_called_once_with("1+2")
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(3, tree.evaluate())
        
    def test_parses_a_minus(self):
        tree = self.parse_expression("1-2", "1 2 -")
        
        self.mock.transform.assert_called_once_with("1-2")
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(-1, tree.evaluate())

    def test_parses_a_multiplication(self):
        tree = self.parse_expression("2*3", "2 3 *")
        
        self.mock.transform.assert_called_once_with("2*3")
        self.assertEqual(2, tree.left.evaluate())
        self.assertEqual(3, tree.right.evaluate())
        self.assertEqual(6, tree.evaluate())   
        
    def test_parses_a_division(self):
        tree = self.parse_expression("1/2", "1 2 /")
        
        self.mock.transform.assert_called_once_with("1/2")
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())
        self.assertEqual(0.5, tree.evaluate())     
        
    def test_parses_complex_no_brackets(self):
        tree = self.parse_expression("1+2/8", "1 2 8 / +")
                   
        self.mock.transform.assert_called_once_with("1+2/8")
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.left.evaluate())
        self.assertEqual(8, tree.right.right.evaluate())
        self.assertEqual(1.25, tree.evaluate())    
        
    def test_parses_complex_with_brackets(self):
        tree = self.parse_expression("(2+7)*4", "2 7 + 4 *")
        
        self.mock.transform.assert_called_once_with("(2+7)*4")
        self.assertEqual(2, tree.left.left.evaluate())
        self.assertEqual(7, tree.left.right.evaluate())
        self.assertEqual(4, tree.right.evaluate())
        self.assertEqual(36, tree.evaluate()) 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()