[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)
```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
import math

def Clean(s):
    """Converts dollar amounts to integers."""
    try:
        return int(s.lstrip('$').replace(',', ''))
    except ValueError:
        if s == 'Under':
            return 0
        elif s == 'over':
            return np.inf
        return None


def ReadData(filename='hinc06.csv'):
    """Reads filename and returns populations in thousands
    filename: string
    returns: pandas Series of populations in thousands
    """
    data = pandas.read_csv(filename, header=None, skiprows=9)
    cols = data[[0, 1]]
        
    res = []
    for _, row in cols.iterrows():
        label, freq = row.values
        freq = int(freq.replace(',', ''))

        t = label.split()
        low, high = Clean(t[0]), Clean(t[-1])

        res.append((high, freq))

    df = pandas.DataFrame(res)
    df.loc[0, 0] -= 1
    df[2] = df[1].cumsum()
    total = df[2][41]
    df[3] = df[2] / total
    df.columns = ['income',  'freq', 'cumsum', 'ps']
    return df

def InterpolateSample(df, log_upper=6.0):
    """Makes a sample of log10 household income.
    Assumes that log10 income is uniform in each range.

    df: DataFrame with columns income and freq
    log_upper: log10 of the assumed upper bound for the highest range

    returns: NumPy array of log10 household income
    """
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)
    df.loc[0, 'log_lower'] = 3.0
    df.loc[41, 'log_upper'] = log_upper
    
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)

    log_sample = np.concatenate(arrays)
    return log_sample

def mycdf(data):
    bins = np.arange(np.int(data.min()),np.int(data.max())+1)
    y, x = np.histogram(data, bins=bins, density=1)
    cumsum=np.concatenate((np.array([0]), np.cumsum(y)))
    plt.plot(x,cumsum,'.') #CDF
    plt.show()
    return None

def mypdf(data):
    y, x = np.histogram(data)
    plt.plot(x[:-1],y/y[0],'.') 
    plt.show()
    return None

def sample_skewness(data):
    mean = np.mean(data)
    moment = sum((x - mean)**3 for x in data) / len(data)
    stdev = np.std(data)
    return moment/(stdev**3)

def main():
    df = ReadData()
    log_sample = InterpolateSample(df, log_upper=6.0)
    data = np.array([10**x for x in log_sample])
    mycdf(data)
    mypdf(data)
    print('mean', np.mean(data))
    print('median', np.median(data))
    print('st dev', np.std(data))
    print('sample skewness', sample_skewness(data))
    print('pearson', 3 * (np.mean(data) - np.median(data)) / np.std(data))

if __name__ == "__main__":
    main()
  ```
