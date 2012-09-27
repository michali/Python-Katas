'''
Created on 26 Sep 2012

@author: Michali
'''
import unittest
import BowlingGame

class GameTests(unittest.TestCase):

    def test_calculates_for_no_strike(self):
        game = BowlingGame.Game()
        noOfStruckPins = 5
        
        score = game.roll(noOfStruckPins)
        
        self.assertEqual(score, noOfStruckPins)

if __name__ == "__main__":
    unittest.main()