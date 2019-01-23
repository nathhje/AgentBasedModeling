# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:45:28 2019

@author: my favorite team
"""

import random

class Agent():
    
    def __init__(self):
        
        self.score = 0
        self.choice = False
        
        self.score_list = []
        self.history = []
        
    def choose(self):
        
        self.choice = bool(random.getrandbits(1))
        
        self.history.append(self.choice)
        
        return self.choice
    
    def outcome(self, winner):
        
        if self.choice == winner:
            
            self.score += 1
            
        self.score_list.append(self.score)
        
    def print_outcomes(self):
        print("The score list and history of this agent.")
        print(self.score_list)
        print(self.history)
