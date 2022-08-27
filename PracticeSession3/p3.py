T = int(input())

def move(Sr, Sc, d, visited):
    visited.append((Sr, Sc))

    if d=='N':
        Sr -=1
    if d=='S':
        Sr +=1
    if d=='E':
        Sc +=1
    if d=='W':
        Sc -=1

    # keep moving
    if (Sr, Sc) in visited:
        Sr, Sc = move(Sr, Sc, d, visited)
    
    return Sr, Sc

def solve(N, R, C, Sr, Sc, D):
    visited = []

    for d in D:
        Sr, Sc = move(Sr, Sc, d, visited)

    return f"{Sr} {Sc}"

for t in range(T):
    N, R, C, Sr, Sc = map(int, input().split())
    D = input()
    print('Case #{}: {}'.format(t+1, solve(N, R, C, Sr, Sc, D)))