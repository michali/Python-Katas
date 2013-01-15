'''
Created on 15 Jan 2013

@author: Michali
'''
import unittest
import re

class ReversePolishNotationConverter(object):    
    
    def __init__(self):
        self.oppattern = re.compile("\+")
        self.numpattern = re.compile("\d")
    
    def convert(self, infix):
        ops = self.oppattern.findall(infix)
        nums = self.numpattern.findall(infix)
        
        return ''.join(nums) + ''.join(ops)


class ReversePolishNotationConverterTests(unittest.TestCase):

    def setUp(self):
        self.converter = ReversePolishNotationConverter()

    def test_convertsOne(self):
        infix = "1+2"
        polish = "12+"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)
        
    def test_convertsTwo(self):
        infix = "1+2+3"
        polish = "123++"
            
        actual = self.converter.convert(infix)
        
        self.assertEqual(polish, actual)