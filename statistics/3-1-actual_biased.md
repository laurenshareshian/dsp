[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nsfg

%matplotlib inline

resp = nsfg.ReadFemResp()
df=pd.DataFrame(resp, columns=['numkdhh'])
lst=[]
biased_lst=[]
for x, p in df.numkdhh.value_counts().sort_index().items():
        print(x,p)
        for i in range(1,p+1):
            lst.append(x)
        for i in range(1,x*p+1):
            biased_lst.append(x)        
df=pd.DataFrame(lst, columns=['data'])
df2=pd.DataFrame(biased_lst, columns=['biased_data'])
fig, ax = plt.subplots()     
ax.hist([df['data'].sort_index(), df2['biased_data'].sort_index()],rwidth=.5, bins=np.arange(-.5,6.5,1) ,normed=1,  label=['data', 'biased_data'])
ax.set_xlabel('Bins', size=20)
ax.set_ylabel('Frequency', size=20)
ax.set_xticks(np.arange(0,7,1))
ax.legend()
print('data mean', df.data.mean())
print('biased mean', df2.biased_data.mean())
```
