'''
Created on 4 Nov 2012

@author: Michali
'''
from Node import OperatorNode, ValueNode


class NodeParser():
           
    def parse(self, expression):
        rpn_exp = self.__convert_to_rpn(expression)
        buffer = []
        for token in rpn_exp:
            if self.__is_number(token):
                buffer.append(ValueNode(int(token)))
            else:
                operator_node = self.__create_operator_node(token)
                operator_node.right = buffer.pop()
                operator_node.left = buffer.pop()
                buffer.append(operator_node)
                
       
    def __convert_to_rpn(self, expression):
        pass
    
    def __create_operator_node(self, token):
        pass