import sys

import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt(sys.stdin)

print(x.max())
print(x.min())
# plt.style.use('ggplot')
# plt.style.use('bmh')

# for style in plt.style.available:
# plt.style.use(style)
# plt.style.use('ggplot')
# plt.yscale('log')
n, bins, patches = plt.hist(x, 100, density=True, facecolor='g', alpha=0.75)
n, bins, patches = plt.hist(x * 2, 100, density=True, facecolor='b', alpha=0.75)

plt.xlabel('Latency')
plt.ylabel('#')
plt.title('Elapsed time')
plt.grid(True)
plt.show()
