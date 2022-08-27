from itertools import permutations

def valid(S):
    seen = {}

    for i in range(len(S)):
        if S[i] in seen and seen[S[i]] != i-1:
            return False
        else:
            seen[S[i]] = i

    return True


def solve(S):
    perms = permutations(S)
    for perm in perms:
        if valid(''.join(perm)):
            return ''.join(perm)

    return 'IMPOSSIBLE'

ANS = "IMPOSSIBLE"

def recc(S, rem):
    global ANS

    if len(rem) == 0:
        return S

    for r in rem:
        if valid(S + r):
            ans = recc(S + r, rem[:rem.index(r)] + rem[rem.index(r)+1:])
            if ans != "IMPOSSIBLE":
                return ans
        
        if valid(r + S):
            ans = recc(r + S, rem[:rem.index(r)] + rem[rem.index(r)+1:])
            if ans != "IMPOSSIBLE":
                return ans

    return "IMPOSSIBLE"
        
T = int(input())
for t in range(T):
    ANS = "IMPOSSIBLE"

    N = int(input())
    S = input().split()

    ans = recc(S[0], S[1:]) # TLE for Test Set 2
    # ans = solve_iterative(D) # TLE for Test Set 2
    print('Case #{}: {}'.format(t+1,ans))

