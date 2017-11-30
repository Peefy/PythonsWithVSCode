

import numpy as np
import matplotlib.pylab as mat

X = np.linspace(np.pi, np.pi, 256, endpoint=True)
C, S = np.sin(X), np.cos(X)

mat.plot(X, C)
mat.show()
