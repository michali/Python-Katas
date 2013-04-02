'''
Created on 17 Jan 2013

@author: Michali
'''
import unittest
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
    
    def __is_open_parentheses(self, current):
        return current == "("    
    
    def __is_closed_parentheses(self, current):
        return current == ")"    
    
    def __handle_open_parentheses(self):
        pass    
    
    def __handle_closed_parentheses(self):
        pass    
    
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
    
    def __append_all_previous_tokens(self):
        while self.__there_are_previous_tokens():
            self.__append_previous_token()  
              
    def __there_are_previous_tokens(self):
        return len(self.__previousTokens) > 0

    def __append_previous_token(self):
        if self.__there_are_previous_tokens():
            self.__append_token(self.__previousTokens.pop())     

    def __handle_operator(self, current):
        while self.__previous_executed_before(current):
            self.__append_previous_token()
        self.__previousTokens.append(current)
    
    def __previous_executed_before(self, current):
        if self.__there_are_previous_tokens():    
            previousPrecedence = self.__calculate_precedence(self.__peek(self.__previousTokens))
            currentPrecedence = self.__calculate_precedence(current)        
            return previousPrecedence >= currentPrecedence
        return False
    
    def __calculate_precedence(self, current):
        if current == "*" or current == "/":
            return 100
        return 1
    
    def __peek(self, stack):
        lastval = stack.pop()
        stack.append(lastval)
        return lastval    
    
    def __append_token(self, token):
        if (len(self.__result) > 0 and len(token) > 0):
            self.__result += " "
        self.__result += token;

    def __is_literal(self, current):
        return re.match("(\w+|\d+)", current) != None
    
class ReversePolishNotationConverterTests(unittest.TestCase):

    def test_EmptyExpressionResultsInSame(self):
        self.when("")
        self.then("")       
        
    def test_NoneProducesEmptyResult(self):
        self.when(None)
        self.then("")
        
    def test_OneNumberResultInSameNumber(self):
        self.when("2")
        self.then("2")        
        
    def test_HandlesASingleBinaryOperator(self):
        self.when("1 + 2")
        self.then("1 2 +")
        
    def test_HandlesMultipleOperatorsOfSamePrecedence(self):
        self.when("a - 5 + 3")
        self.then("a 5 - 3 +")

    def test_HandlesMultipleOperatorsOfDifferentPrecedence_Multiply(self):
        self.when("a - 5 * 3")
        self.then("a 5 3 * -")
        
    def test_HandlesMultipleOperatorsOfDifferentPrecedence_Division(self):
        self.when("a - 5 / 3")
        self.then("a 5 3 / -")
        
    def test_HandlesMultipleOperatorsOfDifferentPrecedence_All_Four(self):
        self.when("a + 5 / 3 - 2 * 8")
        self.then("a 5 3 / + 2 8 * -")
        
    def test_RemovesUnneccessaryParameters(self):
        self.when("( a * 3 ) + 4")
        self.then("a 3 * 4 +")
            
    def setUp(self):
        self.converter = ReversePolishNotationConverter()
        
    def when(self, expression):
        self.result = self.converter.transform(expression)
        
    def then(self, expected):
        self.assertEqual(self.result, expected)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()