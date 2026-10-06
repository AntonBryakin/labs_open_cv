import numpy as np

A = np.ones(3)*1
B = np.ones(3)*2

def f():
	return np.multiply(np.add(A, B), np.divide(-A, 2))

print(f())