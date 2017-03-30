import re
import string

with open('faculty.csv') as f:
    firstline=f.readline() #removes header

    degree_counts=dict()
    title_counts = dict()
    email_list=[]
    email_counts=dict()

    for line in f:
        #count types of degrees
        degree=line.strip().split(',')[1]
        degree=degree.lower()
        translation = str.maketrans("", "", string.punctuation)
        degree = degree.translate(translation)
        for word in degree.split():
            if word not in degree_counts:
                degree_counts[word] = 1
            else:
                degree_counts[word] += 1

        #count types of titles
        title=line.strip().split(',')[2]
        translation = str.maketrans("", "", string.punctuation)
        title = title.translate(translation)
        remove_list=['of', 'is', 'biostatistics']
        remove = '|'.join(remove_list)
        regex = re.compile(r'\b(' + remove + r')\b', flags=re.IGNORECASE)
        title = regex.sub("", title)
        if title not in title_counts:
            title_counts[title] = 1
        else:
            title_counts[title] += 1


        #store email address in list
        email=line.strip().split(',')[3]
        email_list.append(email)

#sort the degree dictionary by value
degree_lst=list()
for key,val in degree_counts.items():
    degree_lst.append((val, key))

degree_lst.sort(reverse = True)

print(str(len(degree_lst))+' types of degrees')
for key,val in degree_lst:
    print (key, val)

#sort the title dictionary by value
title_lst=list()
for key,val in title_counts.items():
    title_lst.append((val, key))

title_lst.sort(reverse = True)

print(str(len(title_lst))+' types of titles')
for key,val in title_lst:
    print (key, val)

#print email list
email_file = open('advanced_python_csv.py', 'w')
for email in email_list:
    email_file.write(email+'\n')
    domain=re.findall('@\S+', email)[0]
    if domain not in email_counts:
        email_counts[domain] = 1
    else:
        email_counts[domain] += 1

print(str(len(email_counts))+' types of domains')
print(email_counts)

