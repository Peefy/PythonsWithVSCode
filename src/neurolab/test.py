
import numpy as np  
import matplotlib.pyplot as plt  
import neurolab as nl  
if __name__ == '__main__':
    import dataset
else: 
    from . import dataset

x = np.linspace(-5, 5, 100)
y = np.sin(x)
plt.plot(x, y)
ax = plt.gca()  
ax.set_xticks(np.linspace(-5,5,11))  
ax.set_xticklabels( ('-5', '-4', '-3', '-2', '-1',  '0',  '1',  '2', '3', '4', '5'), 
    fontdict=dataset.font)  
ax.set_yticks(np.linspace(-1,1,11))  
ax.set_yticklabels( ('-1', '-0.8', '-0.6', '-0.4', '-0.2','0','0.2','0.4', '0.6', '0.8', '1'), 
     fontdict=dataset.font)  
ax.set_ylabel('Error', fontdict=dataset.font)  
ax.set_xlabel('Epochs', fontdict=dataset.font)
plt.show()

# python python/test.py
# python3 python/test.py