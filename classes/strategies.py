# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:48:08 2019

@author: Gebruiker

This file does not work yet at all.
"""
import random

class Strategies():
    
    def __init__(self):
        
        self.idont = "know an init"
        
    def random_strat(self,history_self,history_all):
        
        self.choice = bool(random.getrandbits(1))
        
        self.history.append(self.choice)
        
        return self.choice