import math
import random
import numpy as np
import matplotlib.pyplot as plt
from termcolor import *
import jsoneng
import micrograd.engine

def f(x):
    return x * 2

h = 0.0001

input('''
def f(x):
    return x * 2

h = 0.0001
''')

input('(f(4+h) - f(4))/h')

input("what do you think this evaluates to?")

input((f(4+h) - f(4))/h)

input('h')

input("what is h exactly?")

input("a very small number")

input('dy/dx in f(x)')

input("what is dy/dx exactly?")

input('change on h at x in f(x)')

input('change on a very small number at x in f(x)')

input('next, number example')

input('(2*4 - 2*4 + 2*h)/h in f(x)')

input('(2*h)/h in f(x)')

input('(2*(1/1) in f(x)')

input('at 0, how much would an increase be scaled to')

input('even though we were at x, forget x, go to 0, how much would an increase for a small change be scaled to')
