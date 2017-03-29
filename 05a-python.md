# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> A list is a sequence of values. Lists are mutable, because you can change the order of items in a list or reassign an item in a list. Any integer expression can be used as an index.   A tuple is a sequence of values much like a list, andis also indexed by integer values. Unlike lists, though, tuples are immutable. Tuples are comparable and hashable so we can sort lists of them and use tuples as key values in Python dictionaries.    
---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets can't contain duplicates. Sets are unordered. To find an element in a set, a hash lookup is used, which makes finding an element in a set a lot more efficient than finding it in a list. However, sets are slower than lists when it comes to iterating over their contents. Sets can only contain hashable items.   
As an example, if you let mylist=['hello', 'hello', 'goodbye'], then myset=set(mylist) will contain only one instance of hello and goodbye.
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are a way to create functions without a name. They are often used with the functions filter(), map(), and reduce(). For example,  
'''python
f = lambda x, y : x+y
f(1,1)
'''
returns the number 2.   
As another example,  
'''python 
f=lambda a, b: a if (a > b) else b  
reduce(f, [47, 11, 42, 102, 13])
'''
finds the maximum of the given list.  
As another example,  
'''python
reduce(lambda x, y: x+y, range(1,101))
'''
calculates the sum of numbers from 1 to 100.
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





