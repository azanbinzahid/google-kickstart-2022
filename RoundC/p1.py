from curses.ascii import islower
from math import pi

T = int(input())


def solve(old_pass):
    new_pass = old_pass

    if not any([s.islower() for s in old_pass]):
        new_pass += 'a'

    if not any([s.isupper() for s in old_pass]):
        new_pass += 'A'

    if not any([s.isdigit() for s in old_pass]):
        new_pass += '1'


    if not any([s in ['#', '@', '*', '&'] for s in old_pass]):
        new_pass += '#'

    
    if len(new_pass) < 7:
        new_pass += '@' * (7 - len(new_pass))
    
    return new_pass





for t in range(T):

    N = int(input())
    old_pass = input()

    print('Case #{}: {}'.format(t+1, solve(old_pass)))