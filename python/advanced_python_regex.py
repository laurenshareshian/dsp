import re
import string

f = open('faculty.csv')


counts=dict()
for line in f:
    degree=line.strip().split(',')[1]
    degree=degree.lower()
    translation = str.maketrans("", "", string.punctuation)
    degree = degree.translate(translation)
    for word in degree.split():
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#sort the dictionary by value
lst=list()
for key,val in counts.items():
    lst.append((val, key))

lst.sort(reverse = True)

print(str(len(lst))+' types of degrees')
for key,val in lst:
    print (key, val)

#fac_data=[]
# translation = str.maketrans("", "", string.punctuation)
#
# degrees=[]
# for i in range(2,len(fac_data)):
#     fac_data[i][1]=fac_data[i][1].lower()
#     fac_data[i][1]=fac_data[i][1].translate(translation)
#     for word in fac_data[i][1].split():
#         degrees.append(word)
#
# unique_degrees=set(degrees)
# for degree in unique_degrees:
#     print(degree, degrees.count(degree))