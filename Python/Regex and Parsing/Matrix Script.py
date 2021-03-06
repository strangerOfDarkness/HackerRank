# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/matrix-script/problem
# Difficulty: Hard
# Max Score: 100
# Language: Python

# ========================
#         Solution
# ========================

import re

n, m = map(int, input().split())
a, b = [], ''
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += ''.join(z)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', b))