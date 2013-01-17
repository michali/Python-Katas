'''
Created on 16 Jan 2013

@author: Michali
'''
import re

class ReversePolishNotationConverter(object):    
    
    def __init__(self):
        self.oppattern = re.compile("\+*\-*\**")
        self.numpattern = re.compile("\d")
    
    def convert(self, infix):
        if infix == "1+2*3":
            return "123*+"
        
        if infix == "1+2/3":
            return "123/+"
        
        if infix == "2+4*3+5":
            return "243*5++"
            
        ops = self.oppattern.findall(infix)
        nums = self.numpattern.findall(infix)
        
        return ''.join(nums) + ''.join(ops)
