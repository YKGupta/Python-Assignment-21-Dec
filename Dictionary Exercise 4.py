# Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
l = list(defaults.items())
d = {}
for i in range(len(employees)):
    temp = {}
    for j, k in defaults.items():
        temp[j] = k
    d[employees[i]] = temp
print(d)