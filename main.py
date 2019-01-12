# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.model import Model

def main():
    
    modelA = Model()
    modelA.make_agents(10)
    modelA.run_simulation()

    print(modelA.winner_history)
    
if __name__ == "__main__":
    main()