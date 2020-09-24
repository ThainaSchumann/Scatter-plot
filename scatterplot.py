import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 51, 100)
y = np.random.randint(1, 101, 100)

col = range(50, 150)

mean = np.repeat(y.mean(), 100)
print(mean)

plt.scatter(x, y, label='scatter', marker='*', s=200,
            c=col, cmap='rainbow', alpha=0.5, edgecolor='r')


plt.plot(np.sort(x), mean, color='k', label='Mean')
plt.colorbar(label='Randomly Generated')
plt.legend(loc= 'upper right')
plt.show()
