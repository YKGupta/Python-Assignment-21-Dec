# Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
l = list(sample_dict.values())
minn = l[0]
minPos = 0
for i in range(len(l)):
    if(minn > l[i]):
        minn = l[i]
        pos = i
print(list(sample_dict.keys())[pos])
