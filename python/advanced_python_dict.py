with open('faculty.csv') as f:
    firstline=f.readline() #removes header

    faculty_dict=dict()
    professor_dict=dict()


    for line in f:
        name=line.strip().split(',')[0]
        last_name=name.split()[-1]
        first_name=name.split()[0]
        degree=line.strip().split(',')[1]
        title=line.strip().split(',')[2]
        email=line.strip().split(',')[3]

        #make faculty dictionary
        if last_name not in faculty_dict:
            faculty_dict[last_name]=[degree, title, email]
        else:
            faculty_dict[last_name] = [faculty_dict[last_name]]+[[degree, title, email]]

        #make professor dictionary
        if (first_name, last_name) not in professor_dict:
            professor_dict[(first_name, last_name)] = [degree, title, email]
        else:
            professor_dict[(first_name, last_name)] = professor_dict[(first_name, last_name)]  + [[degree, title, email]]

#print faculty dictionary
for item in faculty_dict:
    print(item, faculty_dict[item])

#print professor dictionary by first name alphabetically
for item in sorted(professor_dict, key = lambda x: x[0]):
    print(item, professor_dict[item])

#print professor dictionary by last name alphabetically
for item in sorted(professor_dict, key = lambda x: x[-1]):
    print(item, professor_dict[item])
