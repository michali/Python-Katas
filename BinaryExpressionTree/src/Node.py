'''
Created on 14 Oct 2012

@author: Michali
'''

class ValueNode:

    def __init__(self, value):
        self.___value = float(value)
        
    def evaluate(self):
        return self.___value

class OperatorNode(object):
    
    def __init__(self, operation):
        self.__operation = operation      
        
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, node):
        self.__right = node
    
    def evaluate(self):
        return self.__operation(self.__left.evaluate(), self.__right.evaluate())