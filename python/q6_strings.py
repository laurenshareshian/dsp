# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'

    raise NotImplementedError

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """
    if len(s) < 2:
        return ''
    else:
        return s[0:2]+s[len(s)-2:len(s)]

    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    """

    new_string=s.replace(s[0], '*')
    return s[0]+new_string[1::]

    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    """

    return b[0:2]+a[2::]+' '+a[0:2]+b[2::]

    raise NotImplementedError

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    """
    if len(s) < 3:
        return s
    else:
        if s[len(s)-3:len(s)]=='ing':
            return s + 'ly'
        else:
            return s + 'ing'

    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    """
    import string

    translation = str.maketrans("", "", string.punctuation)
    s=s.translate(translation)
    word_list=s.split()

    try:
        not_index = word_list.index('not')
        bad_index = word_list.index('bad')
    except:
        return s

    if not_index < bad_index:
        first_string = ' '.join(word_list[0:not_index])
        second_string=' '.join(word_list[bad_index+1::])
        return ' '.join([first_string, 'good', second_string])
    else:
        return s

    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """

    length = lambda x: int(x/2) if x % 2 ==0 else int(x/2)+1
    return a[0:length(len(a))]+b[0:length(len(b))]+a[length(len(a))::]+b[length(len(b))::]

    raise NotImplementedError

