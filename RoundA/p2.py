T = int(input())


def solve(n):
    n = str(n)
    candidates = set()
    curr_sum = sum(map(int, n))
    for i in range(10):
        if (curr_sum+i) % 9 == 0:
            for j in range(len(n)+1):
                new = int(n[:j]+str(i)+n[j:])
                if new != int(n):
                    candidates.add(int(new))

    # print(candidates)
    return min(candidates)



for t in range(T):

    N = int(input())

    print('Case #{}: {}'.format(t+1, solve(N)))