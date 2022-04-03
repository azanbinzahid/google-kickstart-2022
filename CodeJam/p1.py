T = int(input())


def make_row(R, C):
    line1 = '+-' * C + '+'
    line2 = '|.' * C + '|'

    if R == 0:
        line1 = list(line1)
        line2 = list(line2)

        line1[0:2] = '..'
        line2[0:2] = '..'


        line1 = ''.join(line1)
        line2 = ''.join(line2)

    return line1 + '\n' + line2


for t in range(T):
    R, C = map(int, input().split())
    ans = ""

    for r in range(R):
        ans += (make_row(r, C)) + '\n'

    ans+= '+-' * C + '+'

    print(f"Case #{t+1}:\n{ans}")