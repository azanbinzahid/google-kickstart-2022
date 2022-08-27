T = int(input())

def solve(N, AB, P):
    gBus = []
    for i in range(0, len(AB), 2):
        gBus.append((AB[i], AB[i+1]))

    ans = []
    for p in P:
        count = 0
        for b in gBus:
            start, end = b
            count += 1 if (start <= p <= end) else 0
        ans.append(str(count))

    return " ".join(ans)

for t in range(T):
    N = int(input())
    AB = list(map(int, input().split()))
    num_P, P = int(input()), []
    for i in range(num_P):
        P.append(int(input()))

    # empty line b/w test cases
    if t != T-1:
        _ = input()

    print('Case #{}: {}'.format(t+1, solve(N, AB, P)))
