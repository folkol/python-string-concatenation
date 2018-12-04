import sys

import numpy as np
import matplotlib.pyplot as plt
import os

bars = []
height = []
for line in sys.stdin:
    method, time = line.strip().split(',')
    bars.append(method)
    height.append(float(time))

plt.style.use('ggplot')
# Make fake dataset
y_pos = np.arange(len(bars))

# Create horizontal bars
plt.barh(y_pos, height, color='green', alpha=.5, edgecolor='black')

# Create names on the y-axis
plt.yticks(y_pos, bars)
plt.xlabel("Runtime (lower = better)")
plt.title(os.environ.get('TITLE', "Concatenating 20.000 strings"))

# Show graphic
plt.savefig(sys.stdout.buffer, dpi=300)
#plt.show()
