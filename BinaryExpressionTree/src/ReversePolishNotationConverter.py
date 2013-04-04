'''
Created on 4 Apr 2013

@author: michali
'''
import re

class ReversePolishNotationConverter(object):    
        
    def transform(self, expression):               
        self.__initialise(expression)
        
        self.__process_tokens()
        
        return self.__result
    
    def __initialise(self, expression):
        expWithVal = "" if not expression else expression
        self.__tokens = expWithVal.split()
        self.__previousTokens = []
        self.__result = ""
        
    def __process_tokens(self):
        for current in self.__tokens:
            if (self.__is_literal(current)):
                self.__append_token(current)
            elif self.__is_open_parentheses(current):
                self.__handle_open_parentheses()
            elif self.__is_closed_parentheses(current):
                self.__handle_closed_parentheses()
            else:
                self.__handle_operator(current)        
        self.__append_all_previous_tokens()  
    
    def __is_open_parentheses(self, current):
        return current == "("    
    
    def __is_closed_parentheses(self, current):
        return current == ")"    
    
    def __handle_open_parentheses(self):
        self.__previousTokens.append("(")
    
    def __handle_closed_parentheses(self):
        while self.__peek(self.__previousTokens) and self.__peek(self.__previousTokens) != "(":
            self.__append_previous_token()
        
        self.__previousTokens.pop()

    def __append_all_previous_tokens(self):
        while self.__there_are_previous_tokens():
            self.__append_previous_token()  
              
    def __there_are_previous_tokens(self):
        return len(self.__previousTokens) > 0

    def __append_previous_token(self):
        if self.__there_are_previous_tokens():
            self.__append_token(self.__previousTokens.pop())     

    def __handle_operator(self, current):
        while self.__previous_token_has_higher_precedence(current):
            self.__append_previous_token()
        self.__previousTokens.append(current)
    
    def __previous_token_has_higher_precedence(self, current):
        if self.__there_are_previous_tokens():    
            previousPrecedence = self.__calculate_precedence(self.__peek(self.__previousTokens))
            currentPrecedence = self.__calculate_precedence(current)        
            return previousPrecedence >= currentPrecedence
        return False
    
    def __calculate_precedence(self, current):
        if current == "*" or current == "/":
            return 100
        if current == "(" or current == ")":
            return 1
        return 10
    
    def __peek(self, stack):
        if len(stack) > 0:
            return stack[len(stack)-1]    

    def __append_token(self, token):
        if (len(self.__result) > 0 and len(token) > 0):
            self.__result += " "
        self.__result += token;

    def __is_literal(self, current):
        return re.match("(\w+|\d+)", current) != None