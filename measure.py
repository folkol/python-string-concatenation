import sys

import matplotlib.pyplot as plt
import numpy as np

from timeit import timeit, repeat

print(timeit('"".join(ss)', 'ss = [repr(n) for n in range(20000)]', number=1))
sample = repeat('"".join(ss)', 'ss = [repr(n) for n in range(20000)]', number=1, repeat=1000)

plt.style.use('ggplot')
plt.yscale('log')
n, bins, patches = plt.hist(sample, 100, edgecolor='black', density=False, alpha=.5, label='str.join')

sample = repeat('for s in ss: ans += s', 'ans = ""; ss = [repr(n) for n in range(20000)]', number=1, repeat=1000)

plt.style.use('ggplot')
plt.yscale('log')
n, bins, patches = plt.hist(sample, 100, edgecolor='black', density=False, alpha=.5, label='+=')

plt.xlabel('Latency')
plt.ylabel('#')
plt.title(f'Elapsed time str.join')
plt.grid(True)
plt.legend()

plt.show()
