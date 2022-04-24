import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# def calc_palindrome_factors(x):
#     ans = 0

#     for i in range(1,x + 1):
#         str_i = str(i)
#         if (x % i == 0) and (str_i == str_i[::-1]):
#            ans += 1


#     return ans


T = int(input())
for t in range(T):

    N = int(input())

    print('Case #{}: {}'.format(t+1, len(list(filter(lambda x: str(x) == str(x)[::-1], factors(N))))))



