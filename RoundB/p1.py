from math import pi

T = int(input())


def solve(R, A, B):
    sum_areas = 0
    # pi = 22/7
    
    curr_radius = R


    while curr_radius != 0:
        sum_areas += pi * curr_radius**2

        curr_radius *= A
        sum_areas += pi * curr_radius**2

        curr_radius //= B
    
    return sum_areas





for t in range(T):

    R, A, B = map(int, input().split())

    print('Case #{}: {}'.format(t+1, solve(R, A, B)))