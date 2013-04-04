'''
Created on 17 Jan 2013

@author: Michali
'''
import unittest
from ReversePolishNotationConverter import ReversePolishNotationConverter
    
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
        
    def test_NecessaryParenthesesChangeOrderOfEveluation(self):
        self.when("( 3 + 5 ) / 9")
        self.then("3 5 + 9 /")
        
    def test_NecessaryParenthesesChangeOrderOfEveluation_AllFourOperators(self):
        self.when("( 3 - 5 ) * ( 7 + 8 ) / 9")
        self.then("3 5 - 7 8 + * 9 /")
            
    def setUp(self):
        self.converter = ReversePolishNotationConverter()
        
    def when(self, expression):
        self.result = self.converter.transform(expression)
        
    def then(self, expected):
        self.assertEqual(self.result, expected)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()