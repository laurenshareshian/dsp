[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```python
%matplotlib inline
import pandas as pd
import numpy as np
import nsfg

def main():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]
    print('first:', firsts.totalwgt_lb.mean(), 'others:',others.totalwgt_lb.mean())
    print(CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
    #the mean weight of first babies is slightly less than later babies
    #but only by 0.09 standard deviations which is very small
    

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

if __name__ == '__main__':
    main()
```
