'''
Created on 26 Sep 2012

@author: Michali
'''
import unittest
from Game import Game

class GameTests(unittest.TestCase):

    def test_start_score_is_zero(self):
        game = Game()
        
        self.assertEqual(0, game.score)

    def test_calculates_score_no_spare_no_strike(self):
        game = Game()
        noOfStruckPins = 5
        
        game.roll(noOfStruckPins)
        
        self.assertEqual(game.score, noOfStruckPins)
        
    def test_calculates_for_spare(self):
        game = Game()    
        game.roll(5)
        game.roll(5)
        game.roll(3)
        
        self.assertEqual(16, game.score)
        
    def test_calculates_for_strike(self):
        game = Game()  
        game.roll(10)
        game.roll(5)
        game.roll(4)
        
        self.assertEqual(28, game.score)
        
if __name__ == "__main__":
    unittest.main()