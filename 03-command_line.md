# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> >pwd - show current working directory  
mkdir - create directory  
rm -r - remove directory  
touch - creates a file  
rm - removes file  
mv - renames file  
ls -a - lists all files  
cp - copies file  
chmod - modify file access rights  
less - allows you to view text files  
grep - allows you to search for text  
file - tells you what type of item the file is  
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah` 
`ls -t`  
`ls -Glp`  

> > ls - lists non-hidden files  
ls -a - lists all files, including hidden ones  
ls -l - lists all non-hidden contents in long format in bytes  
ls -lh - lists all non-hidden contents in long format in abbreviated size form  
ls -lah - lists all files, including hidden ones, in long form   
ls -t - order files and directories by the time they were last modified.    
ls -Glp - lists all non-hidden contents and highlights folders  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -c displays files by timestamp  
-d displays only directories  
-u displays files by file access time  
-1 displays each entry on a line  
-m displays the names as a comma separated list  
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is a command used to execute commands based on arguments from standard input, and it is helpful when we combine it with other commands.   

For example, to find and remove files ending in .c, we could type: find . -name "*.c" | xargs rm -rf.    
Or, to find occurrences of the text 'stdlib.h' in all of the .c type files, we could type: find . -name '*.c' | xargs grep 'stdlib.h'

 

