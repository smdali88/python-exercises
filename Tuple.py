#Tuble Syntax

"""
Tup = ('Jan','feb','march')

tup1 = ();

Tup1 = (50,);
"""

#Tuple Assignment

"""
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

tup1 = ('Ali','Saif','kjfklj','dfjkkkf')
tup2 = (1,2,3,4,5,6)
print(tup1[1])
print(tup2[0:2])
"""

#Packing and Unpacking

"""
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)
"""

#Comparing tuples

#case 1

"""
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")
"""

#case 2

"""
a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")
"""

#case 3

"""
a=(5,6)
b=(6,4)
if (a>b): print("a is bigger")
else: print("b is bigger")
"""

#Using tuples as keys in dictionaries

"""
directory[last,first] = number

for last, first in directory:

print first, last, directory[last, first]
"""

#Tuples and dictionary

# Dictionary can return the list of tuples by calling items, where each tuple is a key value pair.

"""
a = {'x':100, 'y':200}
c = {'s':2000, 't':3000}
b = list(c.items())
print(c)
"""

"""
a = {'x':100, 'y':200}
c = {'s':2000, 't':3000}
b = list(c.items())
print(a)
"""

#Deleting Tuples

#Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible by using the keyword "del."

#Slicing of Tuple

#To fetch specific sets of sub-elements from tuple or list, we use this unique function called slicing. Slicing is not only applicable to tuple but also for array and list.

"""
x = ("a", "b","c", "d", "e")
print(x[0:4])

x = ("a", "b","c", "d", "e")
print(tuple(x[0])+tuple(x[-2]))

x = ("a", "b","c", "d", "e")
print(x[0:4:3])
"""


#Built-in functions with Tuple

"""
To perform different task, tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.

Advantages of tuple over list
Iterating through tuple is faster than with list, since tuples are immutable.
Tuples that consist of immutable elements can be used as key for dictionary, which is not possible with list
If you have data that is immutable, implementing it as tuple will guarantee that it remains write-protected

"""










