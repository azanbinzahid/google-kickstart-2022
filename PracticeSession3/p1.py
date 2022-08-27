T = int(input())

def solve(N, M, C):
    sum_C = sum(C)
    each_kid = M * (sum_C // M)
    return sum_C - each_kid

for t in range(T):
    N, M = map(int, input().split())
    C = map(int, input().split())
    print('Case #{}: {}'.format(t+1, solve(N, M, C)))