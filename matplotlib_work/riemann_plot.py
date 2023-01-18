import matplotlib.pyplot as plt
import numpy as np
#plt.style.use('_mpl-gallery')

def f(x):
    return x**2
a=2
b=7
dx = (b-a)/2
# make data:
np.random.seed(3)
x = 0.25 + np.arange(16)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 16), xticks=np.arange(1, 16),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()