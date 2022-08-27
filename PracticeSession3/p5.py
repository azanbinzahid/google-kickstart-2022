T = int(input())

# brute force // TLE
def solve(A, B, N, K):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i!=j and ((pow(i, A) + pow(j, B)) % K == 0):
                count += 1

    return count % (pow(10, 9) + 7*(1000000007))

for t in range(T):
    A, B, N, K = map(int, input().split())
    print('Case #{}: {}'.format(t+1, solve(A, B, N, K)))