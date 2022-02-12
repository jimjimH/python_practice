my_tuple = [1, 2, 3, 4, 5, 6]
first, second, *_ = my_tuple

print(first, second, _)
print(type(_))
