T = int(input())



for t in range(T):
    N = int(input())
    D = map(int, input().split())

    D = (sorted(list(D)))

    ans = 1
    for i, d in enumerate(D):
        if d>=ans:
            ans += 1

    print(f"Case #{t+1}: {ans-1}")
