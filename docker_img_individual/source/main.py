import matplotlib.pyplot as plt
import numpy as np

base_number = int(input('insert the base number: '))

x = np.linspace(0, 10, 1000)
y = base_number ** x

plt.plot(x, y)
plt.show()

