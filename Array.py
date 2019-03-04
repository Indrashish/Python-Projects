#Python script for explaining how array works in python

from array import *
from numpy import *

vals = array('i',[10,20,-9,8,6])

#Print out the array
print(vals)

#Print size of the array
print(vals.buffer_info())

#Reverse the array
vals.reverse()
print(vals)

#Create a blank array and take inputs from user
arr = array('i',[])
num_of_elements = int(input("Enter the length of the array"))

for i in range(num_of_elements):
    val = int(input("Enter the next value"))
    arr.append(val)

#Now we have elements in the array, so print out the array
print(arr)

#Multi-dimensional array
arr_mul = array([
                [1,2,3],
                [4,5,6]
            ])

print(arr_mul)