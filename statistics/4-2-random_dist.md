[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)
```python 
import matplotlib.pyplot as plt
import numpy as np
sample = np.random.random(1000)
f, (ax1, ax2) = plt.subplots(1,2)
weights = np.ones_like(sample)/float(len(sample))
ax1 = plt.subplot(131)
ax1.hist(sample, weights=weights, bins=1000)
ax1.set_ylim([0, 0.003])
ax1.set_xlabel('random number')
ax1.set_ylabel('Frequency')
ax2 = plt.subplot(132)
ax2.hist(sample, normed=1, histtype='step', cumulative=True)
ax2.set_ylim([0, 1.1])
ax2.set_xlabel('random number')
ax2.set_ylabel('percentile')
plt.show()
```