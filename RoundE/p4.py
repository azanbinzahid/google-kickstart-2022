T = int(input())

def calc_toll(OP, K, c):

    K = int(K)
    c = int(c)
    if OP == "+":
        return c + K
    if OP == "-":
        return c - K
    if OP == "*":
        return c * K
    if OP == "/":
        return c // K
    

def move(i, j, NN, M, c=0):
    global OPN,N,OPE,E,OPW,W,OPS,S
    
    if M==0:
        return c

    north, south, west, east = 0,0,0,0
    if i-1 >= 0:
        north = move(i-1, j, N, M-1, calc_toll(OPN, N, c))
    if j+1 < NN:
        east = move(i, j+1, N, M-1, calc_toll(OPE, E, c))
    if j-1 >= 0:
        west = move(i, j-1, N, M-1, calc_toll(OPW, W, c))
    if i+1 < NN:
        south = move(i+1, j, N, M-1, calc_toll(OPS, S,c))
    
    return c + max(north, south, west, east, 0)


global OPN,N,OPE,E,OPW,W,OPS,S

for t in range(T):
    NN, P, M, Ar, Ac =  map(int, input().split())
    OPN, N = input().split()
    OPE, E = input().split()
    OPW, W = input().split()
    OPS, S = input().split()
    
    score = move(Ar-1, Ac-1, NN, M)
    print('Case #{}: {}'.format(t+1,score))


# Only Sample Test Case Pass
