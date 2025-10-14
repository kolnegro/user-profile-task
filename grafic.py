import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = 2 * x + 3

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = 2x + 3")
plt.grid(True)
plt.show()