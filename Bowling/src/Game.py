'''
Created on 26 Sep 2012

@author: Michali
'''

class Game:
    
    def __init__(self):
        self.__score = 0
        self.__curFrameIndex = 0
        self.__frames = self.__create_frames()
        
    def __create_frames(self):
        frames = []
        
        r = range(10)
        
        for _ in r:
            frames.append(Frame())
            
        return frames
    
    @property
    def score(self):
        return self.__score
    
    def roll(self, struck_pins):
        self.__add_dropped_pins_to_current_frame(struck_pins)
        
        self.__calc_score(struck_pins) 
        
        if not self.__is_last_frame() and (self.__current_roll_is_second_roll_of_frame() or self.__current_frame_is_strike()):
            self.__curFrameIndex += 1
    
    def __add_dropped_pins_to_current_frame(self, struck_pins):
        self.__frames[self.__curFrameIndex].add_dropped_pins(struck_pins)
        
    def __calc_score(self, struck_pins):        
        if (self.__last_frame_was_a_spare() and self.__current_roll_is_first_roll_of_frame()) or self.__last_frame_was_a_strike():
            self.__score += 2 * struck_pins     
            return
        
        self.__score += struck_pins                

    def __previous_frame(self):
        return self.__frames[self.__curFrameIndex - 1]

    def __last_frame_was_a_spare(self):
        return self.__previous_frame().is_spare()
    
    def __last_frame_was_a_strike(self):
        return self.__previous_frame().is_strike()    

    def __current_frame(self):
        return self.__frames[self.__curFrameIndex]

    def __current_roll_is_first_roll_of_frame(self):
        return self.__current_frame().first_roll_of_frame
    
    def __current_roll_is_second_roll_of_frame(self):
        return self.__current_frame().second_roll_of_frame
    
    def __current_frame_is_strike(self):
        return self.__current_frame().is_strike()
    
    def __current_frame_is_spare(self):
        return self.__current_frame().is_spare()
    
    def __is_last_frame(self):
        return self.__curFrameIndex == 9
        
class Frame:
    
    __no_of_pins = 10
    
    def __init__(self):
        self.__first_roll = 0
        self.__second_roll = 0
        self.__first_roll_of_frame = False
        self.__second_roll_of_frame = False
        
    @property
    def first_roll(self):
        return self.__first_roll
            
    @property
    def second_roll(self):
        return self.__second_roll
            
    def is_spare(self):
        return self.__first_roll + self.__second_roll == self.__no_of_pins
    
    def is_strike(self):
        return self.__first_roll == self.__no_of_pins or self.__second_roll == self.__no_of_pins
    
    @property
    def first_roll_of_frame(self):
        return self.__first_roll_of_frame
    
    @property
    def second_roll_of_frame(self):
        return self.__second_roll_of_frame
    
    def add_dropped_pins(self, no_of_pins):
        if self.__first_roll_of_frame == False:                    
            self.__first_roll = no_of_pins
            self.__first_roll_of_frame = True
        else:
            self.__second_roll = no_of_pins
            self.__first_roll_of_frame = False
            self.__second_roll_of_frame = True