'''
Created on 13 Oct 2012

@author: Michali
'''
import unittest
from Node import OperatorNode
from Node import ValueNode

class ValueNodeTests(unittest.TestCase):

    def test_create_value_node(self):
        node = ValueNode(3)
        
        self.assertEqual(3, node.evaluate())       

class OperatorNodeTests(unittest.TestCase):
    
    def test_evaluate_shallow_node(self):
        node = OperatorNode(lambda x,y: x * y)
        node.left = ValueNode(3)
        node.right = ValueNode(2)
        
        self.assertEqual(6, node.evaluate())
        
    def test_evaluate_deep_operator_node(self):
        node = OperatorNode(lambda x,y: x * y)
        left_node = OperatorNode(lambda x,y : x + y)
        node.left = left_node
        left_node.left = ValueNode(1)
        left_node.right = ValueNode(2)
        node.right = ValueNode(5)
        
        self.assertEqual(15, node.evaluate())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()