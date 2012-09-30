'''
Created on 26 Sep 2012

@author: Michali
'''
import unittest
from Game import Game

class GameTests(unittest.TestCase):

    def test_calculates_score_no_spare_no_strike(self):
        game = Game()
        noOfStruckPins = 5
        
        score = game.roll(noOfStruckPins)
        
        self.assertEqual(score, noOfStruckPins)

if __name__ == "__main__":
    unittest.main()