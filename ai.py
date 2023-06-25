import math
import random
import numpy as np
import matplotlib.pyplot as plt
from termcolor import *
import jsoneng
import micrograd.engine

def f(x):
  return 3*x**2 - 4*x + 5
f(3.0)

xs = np.arange(-5, 5, 0.25)
ys = f(xs)

print(xs)
print(ys)

# plt.plot(xs, ys)
# plt.show()

h = 0.00001
x = 3.0
print((f(x+h) - f(x))/h)
