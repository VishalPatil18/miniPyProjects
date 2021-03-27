# ^	       =>    Matches beggining of line
# $	       =>    Matches the end of the line
# .	       =>    Matches any character
# \s	   =>    Matches whitespaces
# \S	   =>    Matches any non-whitespace char
# *	       =>    Repeates a char zero or more times
# *?	   =>    Repeates a char zero or more times(non-greedy)
# + 	   =>    Repeates a char one or more times
# +? 	   =>    Repeates a char one or more times(non-greedy)
# [aeiou]  =>    Matches a single char in listed set
# [^XYZ]   =>    Matches a single char not in listed set
# [a-z0-9] =>    The set of char can include a range
# (	       =>    Indicates where string extraction is to start
# )	       =>    Indicates where string extraction is to end
import re


def fun1():
    x = 'My 2 fav nums are 18 and 99'
    y = re.findall('[0-9]+', x)
    print(y)
    y = re.findall('[aeiou]+', x)
    print(y)


def fun2():
    x = 'From: using the : chars'
    y = re.findall('^F.+:', x)          # greedy approach prefers the largest string
    print('Greedy: ', y)
    y = re.findall('^F.+?', x)          # non-greedy approach prefers the shortest string
    print('Not Greedy: ', y)


# Fine-Tuning String Extraction
def fun3():
    x = 'From stephen.marq@uct.ac.az Sat Jan  5 09:14:16 2008'
    y = re.findall('\S+@\S+', x)        # greedy approach prefers the largest string
    print(y)
    y = re.findall('\S+@\S+?', x)        # non-greedy approach prefers the shortest string
    print(y)
    y = re.findall('^From (\S+@\S+)', x)
    print(y)


def fun4():
    x = 'From stephen.marq@uct.ac.az Sat Jan  5 09:14:16 2008'
    y = re.findall('@([^ ]*)', x)
    print(y)
    y = re.findall('^From .*@([^ ]*)', x)
    print(y)


def fun5():
    x = 'From stephen.marq*2008.uct.ac.az Sat Jan  5 $09:14:16 2008'
    y = re.findall('\$[0-9]+', x)           # the '\' is used to find the special chars
    print(y)
    y = re.findall('\*([0-9]+)', x)
    print(y)


if __name__ == '__main__':
    fun4()
