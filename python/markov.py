#!/usr/bin/env python

# Markov text generator, [markov.py](python/markov.py). This program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

#I wrote this chatbot using this link: http://stackoverflow.com/questions/5306729/how-do-markov-chain-chatbots-work

import random
import re
import string
import sys

text = str(sys.argv[1]) #text to read
total_words = int(sys.argv[2]) #maximum words?


linestring = open(text, 'r').read()
linestring = re.sub(r"\n", " ", linestring) #get rid of new lines
linestring = re.sub(r"\"", "", linestring) #get rid of quotation marks
words=linestring.split()


#generate key/value pairs of phrases of a given length and the words that follow those phrases
num_of_words=2
word_dict=dict()

for i in range(len(words)-num_of_words):
    phrase = ' '.join([words[j] for j in range(i, i+num_of_words)])
    if phrase not in word_dict:
        word_dict[phrase]=[words[i+num_of_words]]
    else:
        word_dict[phrase] = word_dict[phrase]+[words[i+num_of_words]]

#pick a random key value to start with
starting_phrase = random.choice(list(word_dict.keys()))
rand_num = random.randint(0, len(word_dict[starting_phrase]) - 1)
words = ' '.join([starting_phrase.capitalize(), word_dict[starting_phrase][rand_num]])
starting_phrase =starting_phrase.split()[1] + ' ' + word_dict[starting_phrase][rand_num]

#run chat_bot
count = num_of_words
while count < total_words:
    try:
        rand_num = random.randint(0, len(word_dict[starting_phrase]) - 1)
        words = ' '.join([words, word_dict[starting_phrase][rand_num]])
        starting_phrase = starting_phrase.split()[1] + ' ' + word_dict[starting_phrase][rand_num]
    except:
        if words[-1] not in string.punctuation: #if we run out of pairs but it isn't the end of a line, make it the end of a sentence.
            words = ''.join([words, '.'])
        starting_phrase = random.choice(list(word_dict.keys())) #generate a new phrase to start a new sentence
        words = ' '.join([words, starting_phrase.capitalize()])

    count=count+1


print(re.search(r'(\A.*)\..+',words).group(1)+'.') #remove any sentence fragments at the end