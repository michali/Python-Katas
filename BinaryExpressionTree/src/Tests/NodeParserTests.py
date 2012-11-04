'''
Created on 4 Nov 2012

@author: Michali
'''
import unittest
from NodeParser import NodeParser


class NodeParserTests(unittest.TestCase):


    def test_parses_plus(self):
        parser = NodeParser()
        
        tree = parser.parse("1+2")
        
        self.assertEqual(3, tree.evaluate())
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()