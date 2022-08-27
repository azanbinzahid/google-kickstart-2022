T = int(input())

def solve(N, V):

    prev_highest = V[0]
    count = 0

    for i in range(N):
        if (i == 0 or prev_highest < V[i]) and (i == N-1 or V[i] > V[i+1]):
            count += 1
            prev_highest = V[i]

    return count

for t in range(T):
    N = int(input())
    V = list(map(int, input().split()))
    print('Case #{}: {}'.format(t+1, solve(N, V)))
