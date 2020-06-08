# zeby korzystac z numpy trzeba w venv zainstalowac numpy: pip install numpy

import numpy as np

tab = np.zeros((5,5))
tab[1:4, 1:4] = 1
print(tab)