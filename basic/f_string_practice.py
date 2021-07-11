'''
time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))
'''
# f-string 教學https://www.youtube.com/watch?v=RtKUsUTY6to&feature=youtu.be&t=606

print(f'A:{1:+.2f}|{-2:.2f}|B:{3:0>10.0f}|{10/2:@>10.2f}|C:{3.499:.0f}|{3.500:.0f}|D:{9999999999:,}|E:{3.1415:5.4}')
# >>> A:+1.00|-2.00|B:0000000003|@@@@@@5.00|C:3|4|D:9,999,999,999|E:3.142
'''
A: + 顯示出正數
B: ^ > <可控制對齊方式，前方可指定欲填滿的字符
C: 如果不顯示小數位數，則會round up
D: 可用, 顯示出千分位逗點
E: f is telling that it's a float number. If you forget f then it will just print 1 less digit after the decimal.(少掉一個小數位數)
'''

a, b, c = 3.3, 3.5, 3.7
x, y, z = -3.3, -3.5, -3.7

print(f"{'val':>6}|{'int':>6}|{'//':>6}|{'format':>6}")
print(f"{a:>6}|{int(a):>6}|{a//1:>6}|{a:>6.0f}")
print(f"{b:>6}|{int(b):>6}|{b//1:>6}|{b:>6.0f}")
print(f"{c:>6}|{int(c):>6}|{c//1:>6}|{c:>6.0f}")
print(f"{x:>6}|{int(x):>6}|{x//1:>6}|{x:>6.0f}")
print(f"{y:>6}|{int(y):>6}|{y//1:>6}|{y:>6.0f}")
print(f"{z:>6}|{int(z):>6}|{z//1:>6}|{z:>6.0f}")
'''
output:
   val|   int|    //|format
   3.3|     3|   3.0|     3
   3.5|     3|   3.0|     4
   3.7|     3|   3.0|     4
  -3.3|    -3|  -4.0|    -3
  -3.5|    -3|  -4.0|    -4
  -3.7|    -3|  -4.0|    -4

val: do nothing
int: ingnore the decimal values by truncating it
Floor division: return the greatest integer which is less than the value
f-string format: round the value up
'''

'''
long_variable_name = 12
print(f"{long_variable_name=}")
# >>> long_variable_name=12 (only after Python 3.8)
'''

