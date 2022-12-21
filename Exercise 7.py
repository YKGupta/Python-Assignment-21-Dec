# Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
isFirstSubsetOfSecond = first_set.issubset(second_set)
isSecondSubsetOfFirst = second_set.issubset(first_set)
print("First set is subset of second set -", isFirstSubsetOfSecond)
print("Second set is subset of first set -", isSecondSubsetOfFirst)
isFirstSupersetOfSecond = first_set.issuperset(second_set)
isSecondSupersetOfFirst = second_set.issuperset(first_set)
print("First set is superset of second set -", isFirstSupersetOfSecond)
print("Second set is superset of first set -", isSecondSupersetOfFirst)
if(isFirstSubsetOfSecond or isFirstSupersetOfSecond):
    first_set.clear()
elif(isSecondSubsetOfFirst or isSecondSupersetOfFirst):
    second_set.clear()

print("First set", first_set)
print("Second set", second_set)