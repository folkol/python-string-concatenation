import sys

import matplotlib.pyplot as plt
import numpy as np

colors = 'rgbmcb'
# for style in plt.style.available:
style = 'ggplot'
for c, file in enumerate(sys.argv[1:]):
    x = np.loadtxt(file)

    # plt.style.use('ggplot')
    # plt.style.use('bmh')

    # for style in plt.style.available:
    # plt.style.use(style)
    plt.style.use(style)
    plt.yscale('log')
    # n, bins, patches = plt.hist(x, 30, facecolor=colors[c], edgecolor='black', density=False, alpha=0.3, label=file)
    n, bins, patches = plt.hist(x, 100, edgecolor='black', density=False, alpha=.5, label=file)
    # n, bins, patches = plt.hist(x * 2, 100, density=True, facecolor='b', alpha=0.75)

    plt.xlabel('Latency')
    plt.ylabel('#')
    plt.title(f'Elapsed time {style}')
    plt.grid(True)
plt.legend()
plt.show()
