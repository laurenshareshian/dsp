# Hint:  use Google to find python function

from datetime import datetime

####a)

date_format = '%m-%d-%Y'
date_start = datetime.strptime('01-02-2013', date_format)
date_stop = datetime.strptime('07-28-2015', date_format)
delta=date_stop-date_start
print(delta.days)

####b)

date_format = '%m%d%Y'
date_start = datetime.strptime('12312013', date_format)
date_stop = datetime.strptime('05282015', date_format)
delta=date_stop-date_start
print(delta.days)

####c)

date_format = '%d-%b-%Y'
date_start = datetime.strptime('15-Jan-1994'  , date_format)
date_stop = datetime.strptime('14-Jul-2015', date_format)
delta=date_stop-date_start
print(delta.days)

