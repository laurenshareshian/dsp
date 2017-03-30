import re
import string

with open('faculty.csv') as f:
    firstline=f.readline() #removes header

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