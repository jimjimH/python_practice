# mystring="54321"
# mydict = {5:'a',4:'b',3:'c',2:'d',1:'e'}
# mytuple=(5,4,3,2,1)
# mylist=[5,4,3,2,1]
# myset={5,4,3,2,1}
# print(sorted(mystring))
# print(sorted(mydict))
# print(sorted(mytuple))
# print(sorted(mytuple))
# print(sorted(mylist))

from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())