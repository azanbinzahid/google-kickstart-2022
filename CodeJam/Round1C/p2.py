
def solve(E):

    sum_E = sum(E)
    sum_sq_E = sum(e**2 for e in E)
    sum_E_by_2 = 2 * sum_E
    sum_E_pow_2 = pow(sum_E, 2)


    if sum_E == sum_sq_E:
        return 0


    # sum_sq_E = 2*sum_E*x + sum_E**2
    if sum_E_by_2 == 0:
        return 'IMPOSSIBLE'
    ans = (sum_sq_E - (sum_E_pow_2)) / (sum_E_by_2)

    return int(ans) if (ans // 1 == ans) else "IMPOSSIBLE"

T = int(input())
for t in range(T):
    N, K =  map(int, input().split())
    E = list(map(int, input().split()))

    ans = solve(E)
    # ans = solve_iterative(D)
    print('Case #{}: {}'.format(t+1,ans))