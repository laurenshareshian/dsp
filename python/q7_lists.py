# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    """
    count = 0
    for word in words:
        if len(word) >= 2:
            if word[0] == word[len(word)-1]:
                count = count + 1
    return count

    raise NotImplementedError


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    """
    new_list=[]

    words.sort()
    for word in words:
        if word[0]=='x':
            new_list.append(word)

    for word in words:
        if word[0]!='x':
            new_list.append(word)

    return new_list

    raise NotImplementedError


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    """
    output = sorted(tuples, key = lambda x: x[-1])
    return output

    raise NotImplementedError


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    """
    try:
        new_list=[]
        new_list.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                new_list.append(nums[i])
        return new_list
    except:
        return nums

    raise NotImplementedError


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    """

    new_list = []
    count1 = 0
    count2 = 0

    for word in list1:
        if count2!= len(list2): #if there are still words in the second list to check
            if word <= list2[count2]:
                new_list.append(word) #add the current word in the first list
                count1 = count1 + 1

            else:
                while word > list2[count2]:
                    new_list.append(list2[count2]) #while the current word in the first list is alphabetically after the words in the second list, add the words in the second list
                    count2 = count2 + 1
                    if count2 == len(list2): #if you have added all of the second list then stop
                        break
                new_list.append(word) #add the current word in the first list
                count1 = count1 + 1

    if count1 < len(list1): #if you haven't finished the first list then add them all at the end
        for i in range(count1, len(list1)):
            new_list.append(list1[i])

    if count2 < len(list2):  #if you haven't finished the second list then add them all at the end
        for i in range(count2, len(list2)):
            new_list.append(list2[i])

    return new_list

    raise NotImplementedError

