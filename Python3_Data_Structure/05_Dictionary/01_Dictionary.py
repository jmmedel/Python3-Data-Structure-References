


"""

Python - Dictionary

In Dictionary each key is separated from its value by a colon (:), the items are separated by commas, 
and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with 
just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type,
 but the keys must be of an immutable data type such as strings, numbers, or tuples.

Accessing Values in Dictionary
To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. 
Following is a simple example −


"""

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


"""

When the above code is executed, it produces the following result −

dict['Name']:  Zara
dict['Age']:  7

If we attempt to access a data item with a key, which is not part of the dictionary, we get an error as follows −

#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Alice']: ", dict['Alice']
When the above code is executed, it produces the following result −

dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'

"""



