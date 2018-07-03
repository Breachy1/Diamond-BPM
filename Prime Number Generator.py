"""
Created on Tue Jun 26 17:40:47 2018
Author: olliebreach

Description: 
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng


def primes(num):
    prime_nums = []
    for i in range(num):
        count = 0
        for n in range(1, i):
            if i % n == 0:
                count += 1
        if count == 1:
            prime_nums.append(i)
    prime_array = np.asarray(prime_nums)
    return prime_array


            
    


 




