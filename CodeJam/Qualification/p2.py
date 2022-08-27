import numpy as np

T = int(input())



def check_sum(ink_levels):
    D = pow(10, 6)
    
    printers_array = [min(ink_levels[x]) for x in range(4)]

    for i in range(4):
        D -= printers_array[i]

    if D > 0:
        return "IMPOSSIBLE"

    elif D == 0:        
        return " ".join([str(printers_array[i]) for i in range(4)])

    else:
        available = sum(printers_array)+D
        ans = []
        for i in range(4):
            x = (min(available, printers_array[i]))
            if x >= 0:
                ans.append(str(x))
            else:
                ans.append(str(0))

            available -= printers_array[i]

        return " ".join(ans)


for t in range(T):
    # ans = 'IMPOSIBLE'
    ink_levels = []

    for i in range(3):
        Ci, Mi, Yi, Ki = map(int, input().split())
        ink_levels.append([Ci, Mi, Yi, Ki])

    ink_levels = np.array(ink_levels)
    ink_levels = np.transpose(ink_levels)

    ans = check_sum(ink_levels)

    print(f"Case #{t+1}: {ans}")
