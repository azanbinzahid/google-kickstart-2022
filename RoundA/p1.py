T = int(input())

def solve(I, P):
    i = 0
    j = 0
    Y = 0
    for p in P:
        j+=1
        if p == I[i]:
            i+=1
        else:
            Y+=1

        if i==len(I):
            return Y+len(P)-j



    return 'IMPOSSIBLE'

for t in range(T):

    I = input()
    P = input()

    print('Case #{}: {}'.format(t+1, solve(I, P)))