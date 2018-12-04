import sys
from os import environ

import matplotlib.pyplot as plt
import numpy as np


def smooth(y, box_pts):
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


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
    # plt.yscale('log')
    # n, bins, patches = plt.hist(x, 30, facecolor=colors[c], edgecolor='black', density=False, alpha=0.3, label=file)
    # n, bins, patches = plt.hist(x, 100, edgecolor='black', density=False, alpha=.5, label=file)
    # n, bins, patches = plt.hist(x * 2, 100, density=True, facecolor='b', alpha=0.75)

    step = int(environ.get('STEP', '1'))
    plt.plot(range(0, 100 * step, step), x, label=file)
    # plt.xticks([1, 2, 3, 4, 5])

    plt.xlabel('Latency')
    plt.ylabel('#')
    plt.title('Elapsed time')
    plt.grid(True)

plt.legend()
# plt.show()
plt.savefig(sys.stdout.buffer, dpi=300)
