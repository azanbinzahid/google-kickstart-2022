T = int(input())
for t in range(T):

    N = int(input())
    ratings =  list(map(int, input().split()))
    seq = sorted(ratings, reverse=True)
    ans = []

    for r in ratings:
        for s in seq:
            if s <= 2*r:
                if s == r and seq.count(s) == 1:
                    continue
                ans.append(str(s))
                break
        else:
            ans.append("-1")


    ans = " ".join(ans)
    print('Case #{}: {}'.format(t+1,ans))

# Test Case 1 Pass
