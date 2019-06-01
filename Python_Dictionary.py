#Syntax for Python Dictionary:

"""
Dict = { ' Tim': 18,  xyz,.. }
"""

#Properties of Dictionary Keys

"""
There are two important points while using dictionary keys

More than one entry per key is not allowed ( no duplicate key is allowed)
The values in the dictionary can be of any type while the keys must be immutable like numbers, tuples or strings.
Dictionary keys are case sensitive- Same key name but with the different case are treated as different keys in Python dictionaries.
"""

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print (Dict['Tiffany'])


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print((Dict['Robert']))
"""

#Python Dictionary Methods

"""
Copying dictionary
You can also copy the entire dictionary to new dictionary. For example, here we have copied our original dictionary to new dictionary name "Boys" and "Girls".
"""

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)
"""

#Updating Dictionary

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)
"""

#Delete Keys from the dictionary

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
del Dict ['Charlie']
print(Dict)
"""

#Dictionary items() Method

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))
"""

#Check if a given key already exists in a dictionary

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in Dict.keys():
    if key in Boys.keys():
        print(True)
    else:       
        print(False)
"""

#Sorting the Dictionary

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
"""

#Python Dictionary in-built Functions

#Dictionary len() Method

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Length : %d" % len (Dict))
"""

#Variable Types

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("variable Type: %s" %type (Dict))
"""

#Python List cmp() Method

"""
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}	
print(cmp(Girls, Boys))

#or

cmp is not supported in Python 3
"""

#Dictionary Str(dict)

"""
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("printable string:%s" % str (Dict))
"""

#Here is the list of all Dictionary Methods

"""
Method	        Description	                                                        Syntax
copy()	        Copy the entire dictionary to new dictionary	                        dict.copy()
update()	Update a dictionary by adding a new entry or a key-value pair to an
                existing entry or by deleting an existing entry.	                Dict.update([other])
items()	        Returns a list of tuple pairs (Keys, Value) in the dictionary.	        dictionary.items()
sort()	        You can sort the elements	                                        dictionary.sort()
len()	        Gives the number of pairs in the dictionary.	                        len(dict)
cmp()	        Compare values and keys of two dictionaries	                        cmp(dict1, dict2)
Str()	        Make a dictionary into a printable string format	                Str(dict)
"""







