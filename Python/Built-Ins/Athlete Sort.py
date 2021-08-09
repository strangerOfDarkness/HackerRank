# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-sort-sort/problem
# Difficulty: Medium
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================
import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    k = int(input().strip())
    
    for el in sorted(arr, key = lambda x: x[k]):
        print(" ".join(map(str, el)))