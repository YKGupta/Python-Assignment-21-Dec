# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d = {}
for i in sample_list:
    c = 0
    for j in sample_list:
        if(i == j):
            c += 1
    d[i] = c
print("Printing count of each item", d)