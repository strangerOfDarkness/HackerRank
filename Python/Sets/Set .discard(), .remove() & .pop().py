# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    string = input().split()
    if string[0] == 'pop':
        s.pop()
    elif string[0] == 'remove':
        s.remove(int(string[1]))
    elif string[0] == 'discard':
        s.discard(int(string[1]))
print(sum(s))