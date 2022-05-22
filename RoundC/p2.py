from fractions import Fraction

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

T = int(input())
for t in range(T):
    n, X, Y =  map(int, input().split())
    N = set(range(1, n+1))
    ratio = Fraction(X, Y)
    ans = 'IMPOSSIBLE'
    
    POWERSET = powerset(N)

    A = {}
    B = {}

    # brute-force
    for i in POWERSET:
        A = set(i)
        B = N.difference(i)

        if Fraction(sum(A), sum(B)) == ratio:
            ans = 'POSSIBLE\n'
            ans += f'{len(A)}\n'
            ans += ' '.join([str(a) for a in A])
            break
    
    print('Case #{}: {}'.format(t+1,ans))