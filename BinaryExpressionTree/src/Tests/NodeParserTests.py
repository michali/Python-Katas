'''
Created on 4 Nov 2012

@author: Michali
'''
import unittest
from NodeParser import NodeParser

class NodeParserTests(unittest.TestCase):

    def setUp(self):
        self.parser = NodeParser()

    def test_parses_an_operator(self):
        tree = self.parser.parse("1+2")
        
        self.assertEqual(1, tree.left.evaluate())
        self.assertEqual(2, tree.right.evaluate())

    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()