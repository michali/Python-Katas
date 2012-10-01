'''
Created on 30 Sep 2012

@author: Michali
'''
import unittest
from Game import Frame

class Test(unittest.TestCase):

    def test_adds_first_roll(self):
        frame = Frame()
        
        frame.add_dropped_pins(1)
        
        self.assertEqual(1, frame.first_roll)
        
    def test_adds_second_roll(self):
        frame = Frame()
        
        frame.add_dropped_pins(1)
        frame.add_dropped_pins(2)
        
        self.assertEqual(2, frame.second_roll)    
        
    def test_initialise_with_zero_hits(self):
        frame = Frame()
        
        self.assertEqual(0, frame.first_roll)
        self.assertEqual(0, frame.second_roll)
        
    def test_frame_is_spare(self):
        frame = Frame()
        
        frame.add_dropped_pins(2)
        frame.add_dropped_pins(8)
        
        self.assertTrue(frame.is_spare)
        
    def test_frame_is_not_spare(self):
        frame = Frame()
        
        frame.add_dropped_pins(2)
        frame.add_dropped_pins(7)
        
        self.assertFalse(frame.is_spare())

    def test_strike_on_first_roll(self):
        frame = Frame()
        
        frame.add_dropped_pins(10)
        
        self.assertTrue(frame.is_strike())
        
    def test_strike_on_second_roll(self):
        frame = Frame()
        
        frame.add_dropped_pins(0)
        frame.add_dropped_pins(10)
        
        self.assertTrue(frame.is_strike())

    def test_not_strike(self):
        frame = Frame()
        
        frame.add_dropped_pins(1)
        frame.add_dropped_pins(2)
               
        self.assertFalse(frame.is_strike())
        
    def test_is_first_roll_of_frame(self):
        frame = Frame()
        
        frame.add_dropped_pins(1)
        
        self.assertTrue(frame.first_roll_of_frame)
        
    def test_is_second_roll_of_frame(self):
        frame = Frame()
        
        frame.add_dropped_pins(1)
        frame.add_dropped_pins(1)
        
        self.assertTrue(frame.second_roll_of_frame)
        
    def test_frame_not_rolled(self):
        frame = Frame()

        self.assertFalse(frame.first_roll_of_frame)

    def test_second_roll_of_frame(self):
        frame = Frame()
 
        frame.add_dropped_pins(1)
        frame.add_dropped_pins(2)
        
        self.assertFalse(frame.first_roll_of_frame)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
