str = 'Runtime and compile time are programming terms that refer to different stages of software program development. \nCompile-time is the instance where the code you entered is converted to executable while Run-time is the instance where the executable is running. \nThe terms "runtime" and "compile time" are often used by programmers to refer to different types of errors too.'
import csv

arr = [
    ['charater', 'number'],
    ['a', 123],
    ['b', 456],
    ['c', 789],
    ['d', 101112],
    ['e', 131415],
] 

with open('csv_test.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(arr)

with open('csv_test.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    in_str = [row for row in cin]

print(in_str)








'''
f = open('test1.py', mode='w')
# content = f.read()
# print(content)
# print(len(content))
# print(type(content))
# f.write('qqq')
print(str, file=f)
f.close()
'''