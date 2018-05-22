
# python main.py
# python3 main.py

from numpy import *
from numpy.linalg import *
from matplotlib.pyplot import *
import seaborn

seaborn.set_style('darkgrid')

x = arange(0, 10, 0.01)
y = sin(x)
n = norm(y)
plot(x, y)
print(n)
show()

# rand number 2 * 2 * 2
print(random.rand(2, 2, 2))

print('add code runner')

# python main.py
# python3 main.py
