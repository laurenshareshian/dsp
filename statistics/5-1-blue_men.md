[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

from scipy import stats
high = scipy.stats.norm.cdf([185.42], loc = 178, scale = 7.7)
low = scipy.stats.norm.cdf([177.8], loc = 178, scale = 7.7)
print(high-low)