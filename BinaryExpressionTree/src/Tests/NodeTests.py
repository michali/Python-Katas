'''
Created on 13 Oct 2012

@author: Michali
'''
import unittest
from Node import ValueNode

class ValueNodeTests(unittest.TestCase):

    def test_create_numerical_node(self):
        node = ValueNode(3)
        
        self.assertEqual(3, node.evaluate())        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()