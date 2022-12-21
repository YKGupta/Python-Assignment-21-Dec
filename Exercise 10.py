# Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
ans = []
for i in sample_list:
    if i not in ans:
        ans.append(i)
sample_list = ans
print("unique items", sample_list)
print("tuple", tuple(sample_list))
minn = sample_list[0]
maxx = sample_list[0]
for i in sample_list:
    if(minn > i):
        minn = i
    if(maxx < i):
        maxx = i
print("min:", minn)
print("max:", maxx)