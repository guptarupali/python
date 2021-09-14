import numpy as np
import matplotlib.pyplot as py

file = 'digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))