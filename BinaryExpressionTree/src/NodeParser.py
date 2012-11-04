'''
Created on 4 Nov 2012

@author: Michali
'''
from Node import OperatorNode, ValueNode

class NodeParser():
    
    def parse(self, expression):
        tree = OperatorNode(lambda x,y:x+y)
        tree.left = ValueNode(1)
        tree.right = ValueNode(2)
        return tree
