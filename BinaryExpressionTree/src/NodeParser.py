'''
Created on 4 Nov 2012

@author: Michali
'''
from Node import OperatorNode, ValueNode
import re

class NodeParser():    

    def __get_operations(self):
        return dict([("+", lambda x, y : x + y), ("-", lambda x, y : x - y), ("*", lambda x, y : x * y), ("/", lambda x, y : x / y)])
        
    def __init__(self, rpnConverter):
        self.__rpnConverter = rpnConverter       
        self.__buffer = []    
        self.__operations = self.__get_operations()           
    
    def parse(self, expression):
        rpn_exp = self.__convert_to_rpn(expression)

        rpn_tokens = rpn_exp.split()
        for token in rpn_tokens:
            if self.__is_number(token):
                self.__add_value_node_from(token)
            else:                
                self.__add_operator_node_from(token)    
                
        return self.__top_node()     
         
    def __add_node_to_buffer(self, node):
        self.__buffer.append(node)        

    def __add_value_node_from(self, token):
        value_node = ValueNode(int(token))
        self.__add_node_to_buffer(value_node)       

    def __add_operator_node_from(self, token):
        operator_node = OperatorNode(self.__get_operation(token))
        operator_node.right = self.__buffer.pop()
        operator_node.left = self.__buffer.pop()
        self.__add_node_to_buffer(operator_node)    

    def __top_node(self):
        return self.__buffer.pop() 
      
    def __convert_to_rpn(self, expression):
        return self.__rpnConverter.transform(expression)
    
    def __is_number(self, token):
        return re.match("\d+", token) != None
    
    def __get_operation(self, operator_token):
        return self.__operations[operator_token]
            
