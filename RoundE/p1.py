T = int(input())


def solve(N):
    bot = 1
    john = 0
    for i in range(1, N):
        if i%2==0:
            continue
        else:
            if bot < john:
                bot +=1
            else:
                john +=1
    return bot


for t in range(T):

    N = int(input())

    print('Case #{}: {}'.format(t+1, solve(N)))

# Test Case 1 Pass