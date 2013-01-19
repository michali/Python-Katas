'''
Created on 17 Jan 2013

@author: Michali
'''
import unittest


class ShuntingYardAlgorithm(object):    
    
    def transform(self, expression):               
        expWithVal = "" if not expression else expression
        tokenizedExp = expWithVal.split()
        
        if len(tokenizedExp) == 3:
            return "{0} {2} {1}".format(*tokenizedExp)
        
        return expWithVal
    
class Test(unittest.TestCase):

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
        
        
    def setUp(self):
        self.algorithm = ShuntingYardAlgorithm()
        
    def when(self, expression):
        self.result = self.algorithm.transform(expression)
        
    def then(self, expected):
        self.assertEqual(self.result, expected)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()