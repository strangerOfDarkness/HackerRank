# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/validating-uid/problem
# Difficulty: Easy
# Max Score: 40
# Language: Python

# ========================
#         Solution
# ========================

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')