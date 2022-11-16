#!/usr/bin/env python3

import random

def rollDice():
   die1 = random.randint(1,6)
   die2 = random.randint(1,6)

   return die1, die2, die1 + die2

