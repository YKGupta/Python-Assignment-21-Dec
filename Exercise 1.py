# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd = []
even = []
ans = []
for i in range(1, len(l1), 2):
    odd.append(l1[i])
    ans.append(l1[i])

for i in range(0, len(l2), 2):
    even.append(l2[i])
    ans.append(l2[i])

print("Element at odd-index positions from list one")
print(odd)
print("Element at even-index positions from list two")
print(even)

print("Printing Final third list")
print(ans)