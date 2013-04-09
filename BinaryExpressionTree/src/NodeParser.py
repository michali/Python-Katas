'''
Created on 4 Nov 2012

@author: Michali
'''
from Node import OperatorNode, ValueNode
import re

class NodeParser():
    
    def __init__(self, rpnConverter):
        self.__rpnConverter = rpnConverter   
    
    def parse(self, expression):
        rpn_exp = self.__convert_to_rpn(expression)
        buffer = []
        rpn_tokens = rpn_exp.split()
        for token in rpn_tokens:
            if self.__is_number(token):
                buffer.append(ValueNode(int(token)))
            else:
                operator_node = OperatorNode(self.__create_operation(token))
                operator_node.right = buffer.pop()
                operator_node.left = buffer.pop()
                buffer.append(operator_node)      
                
        return operator_node          
       
    def __convert_to_rpn(self, expression):
        return self.__rpnConverter.transform(expression)
    
    def __is_number(self, token):
        return re.match("\d+", token) != None
    
    def __create_operation(self, token):
        if token == "+":
            return lambda x, y : x + y
        if token == "-":
            return lambda x, y : x - y
        if token == "*":
            return lambda x, y : x * y
        return lambda x, y : x / y
            
