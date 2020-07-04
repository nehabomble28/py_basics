# Plot sin(x) and cos(x) functions for values of x between 0 and pi. Use inbuilt libraries numpy and matplotlib.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4 * np.pi, 0.1)

y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, x, z)
plt.show()
