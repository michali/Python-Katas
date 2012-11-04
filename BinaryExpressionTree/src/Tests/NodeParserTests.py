'''
Created on 4 Nov 2012

@author: Michali
'''
import unittest
from Node import OperatorNode, ValueNode


class NodeParser():
    
    def parse(self, expression):
        tree = OperatorNode(lambda x,y:x+y)
        tree.left = ValueNode(1)
        tree.right = ValueNode(2)
        return tree

class NodeParserTests(unittest.TestCase):


    def test_parses_plus(self):
        parser = NodeParser()
        
        tree = parser.parse("1+2")
        
        self.assertEqual(3, tree.evaluate())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()