# https://www.hackerrank.com/challenges/absolute-permutation/problem?h_r=next-challenge&h_v=zen
def absolutePermutation(n, k):
    result = [i for i in range(1, n+1)]
    if k == 0:
        return result
    if n % 2 == 0 and n//2 %k == 0:
        for i in range(n):
            if result[i] == i+1:
                result[i], result[i+k] = result[i+k], result[i]
        return result
    else:
        return [-1]

print(absolutePermutation(12,2))