from functools import reduce

T = int(input())


def solve(A, B):
    ans = 0
    for i in range(A, B+1):
        arr = list(map(int, str(i)))
        if reduce((lambda x, y: x * y), arr) % sum(arr) == 0:
            ans+=1

    return ans



for t in range(T):

    A, B = map(int, input().split())

    print('Case #{}: {}'.format(t+1, solve(A, B)))