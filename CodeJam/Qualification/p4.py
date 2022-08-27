from itertools import permutations

T = int(input())

P = []

def calc_fun(i, F):
    global P
    ans = F[i-1]
    F[i-1] = 0
    if P[i-1] != 0:
        ans = max(ans, calc_fun(P[i-1], F))

    return ans



for t in range(T):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))

    initiators = []
    for i in range(N+1):
        if i not in P:
            initiators.append(i)

    perms = permutations(initiators)
    final_ans = 0
    for perm in perms:
        newF = F.copy()
        ans = 0
        for i in perm:
            ans += calc_fun(i, newF) 
        final_ans = max(ans, final_ans)

    print(f"Case #{t+1}: {final_ans}")
