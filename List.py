#Python script for list

#Creating a list
thislist = ["apple", "banana", "cherry"]
#Creating a set
thisset = {"red", "green", "blue"}

print("Printing the list:")
print(thislist)
print("Printing the set:")
print(thisset)

x = lambda a : a + 10
print(x(5))

#Change the second item of the list
thislist[1] = "blackberry"
print(thislist) #Prints out the list after modification

#Append elements to the list
thislist.append(5)
print(thislist[1])

#Traverse list with a for loop. With this, we also implement for loop
for x in thislist:
    print("Array element = ", x)
for i in range(len(thislist)):
    print("Element at index", i, thislist[i])

#Pop/delete elements from the list
thislist.pop()
print(thislist)

#Remove function
#thislist.remove("mango")
#print(thislist)

thislist.__delitem__(1)
print(thislist)

