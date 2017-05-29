[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---
``` import numpy as np
import math 
import matplotlib.pyplot as plt
import pandas as pd

def MeanError(estimates, actual):
    errors = [estimate-actual for estimate in estimates]
    return np.mean(errors)

def RMSE(estimates, actual):
    e2 = [(estimate-actual)**2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def Percentile(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) // 100
    return scores[index]

def SimulateGame(lam):
    """Simulates a game and returns the estimated goal-scoring rate.

    lam: actual goal scoring rate in goals per game
    """
    goals = 0
    t = 0
    while True:
        time_between_goals = np.random.exponential(1/lam,1)
        t += time_between_goals
        if t > 1:
            break
        goals += 1

    """estimated goal-scoring rate is the actual number of goals scored"""
    L = goals
    return L

def many_games(lam, m=100000):

    estimates = []
    for i in range(m):
        L = SimulateGame(lam)
        estimates.append(L)

    print('rmse L', RMSE(estimates, lam))
    print('mean error L', MeanError(estimates, lam))
    print('5th percentile: ', Percentile(estimates, 5))
    print('95th percentile: ', Percentile(estimates, 95))

    low = min(estimates)
    high = max(estimates)
    lower=Percentile(estimates, 5)
    upper=Percentile(estimates, 95)
    
    df = pd.DataFrame(data=estimates, columns=['goals'])
    df.plot.hist(rwidth=.9, bins=np.arange(low-.5, high-.5,1), normed = 1)
    plt.plot([lower, lower], [0,.3])    
    plt.plot([upper, upper], [0,.3])
    plt.xlabel('goals')
    plt.ylabel('frequency')
    plt.show()
    

          
lam = 2
many_games(lam)

```