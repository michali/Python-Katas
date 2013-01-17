'''
Created on 15 Jan 2013

@author: Michali
'''
import unittest
from ReversePolishNotationConverter import ReversePolishNotationConverter

class ReversePolishNotationConverterTests(unittest.TestCase):

    def setUp(self):
        self.converter = ReversePolishNotationConverter()

    def test_convertsOnePlus(self):
        infix = "1+2"
        polish = "12+"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsOneMinus(self):
        infix = "1-2"
        polish = "12-"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsTwoPluses(self):
        infix = "1+2+3"
        polish = "123++"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsTwoMinuses(self):
        infix = "1-2-3"
        polish = "123--"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsPlusAndMinus(self):
        infix = "1+2-3"
        polish = "123+-"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertPlusAndMultiplication(self):
        infix = "1+2*3"
        polish = "123*+"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertPlusAndDivision(self):
        infix = "1+2/3"
        polish = "123/+"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsPlusMultiplicationPlus(self):
        infix = "2+4*3+5"
        polish = "243*5++"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        