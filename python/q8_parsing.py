# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

f=open('football.csv')
football_data=[]
for line in f:
    football_data.append(line.rstrip().split(','))

smallest_team=football_data[1][0]
smallest=int(football_data[1][5])-int(football_data[1][6])

for i in range(2, len(football_data)):
    if int(football_data[i][5])-int(football_data[i][6]) < smallest:
        smallest_team=football_data[i][0]
        smallest=int(football_data[i][5])-int(football_data[i][6])

print(smallest_team+'has the smallest difference of ' + str(smallest))

