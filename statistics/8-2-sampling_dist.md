[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

``` python
import numpy as np
import math 
import matplotlib.pyplot as plt

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def Percentile(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) // 100
    return scores[index]

def SimulateExpSample(lam=2, n=10, m=1000):
    means = []
    for j in range(m):
        xs = np.random.exponential(1.0/lam,n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / np.median(xs)
        means.append(L)
        
    print('rmse L', RMSE(means, lam))

    print('5th percentile: ', Percentile(means, 5))
    print('95th percentile: ', Percentile(means, 95))
    
    return means, Percentile(means, 5), Percentile(means, 95)

def mycdf(data, low, upp):
    stepsize=0.1
    bins = np.arange(np.int(data.min()),np.int(data.max())+1, stepsize)
    y, x = np.histogram(data, bins=bins, density=1)
    cumsum=np.concatenate((np.array([0]), np.cumsum(y)))
    cumsum = cumsum/cumsum[-1]
    plt.plot(x,cumsum) #CDF
    plt.xlabel('estimate')
    plt.ylabel('CDF')
    plt.title('sampling distribution')
    plt.plot([low,low], [0,1])
    plt.plot([upp,upp], [0,1])
    plt.show()

means, low, upp = SimulateExpSample()
means = np.asarray(means)
mycdf(means, low, upp)
```