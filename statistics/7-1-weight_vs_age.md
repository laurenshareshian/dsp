[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

``` python
import math
import numpy as np
import nsfg
import pandas as pd
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
%matplotlib inline

def BinnedPercentiles(df, minval, maxval, incr_num):
    """Bin the data by age and plot percentiles of weight for each bin.
    df: DataFrame
    """
    bins = np.arange(minval, maxval, incr_num)
    indices = np.digitize(df.agepreg, bins)
    groups = df.groupby(indices)
    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Config(xlabel="Mother's age (years)",ylabel='Birth weight (lbs)',xlim=[14, 45], legend=True)
    plt.show()
    
def Corr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    meanx, varx = MeanVar(xs)
    meany, vary = MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx * vary)
    return corr

def main():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    minweight = live.agepreg.min() - 1
    maxweight = live.agepreg.max() - 1
    numofincrements = 3
    BinnedPercentiles(live, minweight, maxweight, numofincrements)
    
    ages = live.agepreg
    weights = live.totalwgt_lb
    print("Pearson: ",ages.corr(weights, method='pearson'))
    print("Spearman: ", ages.corr(weights, method='spearman'))

    plt.plot(ages, weights,'.', alpha=.1)
    plt.xlabel("mother's age")
    plt.ylabel("birth weight")
    plt.show()
    
if __name__ =='__main__':
    main()
    ```