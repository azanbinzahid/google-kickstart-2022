from itertools import combinations_with_replacement
from typing import Counter

from itertools import permutations


def get_len_palindrome(string):
    all_permutations = [''.join(p) for p in permutations(string)]

    for permutation in all_permutations:
        for i in range(len(permutation)+1):
            if permutation[:i] == permutation[:i][::-1]:
                if i >=5:
                    return True

    return False

T = int(input())


def solve(S):
    count_q_marks = Counter(S)
    comb = combinations_with_replacement([1, 0], count_q_marks['?'])
    
    for c in comb:
        j = 0
        new_S = [s for s in S]
        for i, s in enumerate(S):
            if s == '?':
                new_S[i] = str(c[j])
                j +=1

        if get_len_palindrome(''.join(new_S)):
            return 'IMPOSSIBLE'

    return 'POSSIBLE'

for t in range(T):

    N = int(input())
    S = input()

    print('Case #{}: {}'.format(t+1, solve(S)))