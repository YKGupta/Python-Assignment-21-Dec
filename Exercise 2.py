# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
list1 = [54, 44, 27, 79, 91, 41]
temp = list1[4]
list1.pop(4)
print("List After removing element at index 4", list1)
list1.insert(2, temp)
print("List After adding element at index 2", list1)
list1.append(temp)
print("List after Adding element at last", list1)