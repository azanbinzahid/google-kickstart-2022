
T = int(input())
for t in range(T):
    N, L =  map(int, input().split())
    ants = {}
    ants_at_pos = {}
    ants_at_pos_5 = {}

    for i in range(N):
        P, D = map(int, input().split())
        P = P if D else -P
        ants[i+1] = P
        
        if abs(P) not in ants_at_pos:
            ants_at_pos[abs(P)] = set([i+1])
        else:
            ants_at_pos[abs(P)].add(i+1)

    for p in ants_at_pos.keys():
        if ants_at_pos[p] and len(ants_at_pos[p]) > 1:
            for a in ants_at_pos[p]:
                if a in ants:
                    ants[a] = -1 * ants[a]
 
    # brute-force
    ans = []
    while len(ants):
        ants_at_pos = {}
        semi_ans = []


        for k in range(1, N+1):
            if k in ants:
                ants[k] += 0.5

                abs_pos = abs(ants[k])
                if abs_pos not in ants_at_pos:
                    ants_at_pos[abs_pos] = set([k])
                else:
                    ants_at_pos[abs_pos].add(k)


                if ants[k] == 0 or ants[k] == L:
                    semi_ans.append(k)
                    del ants[k]

        if len(semi_ans):
            ans += (sorted(semi_ans, reverse=False))

        for p in ants_at_pos.keys():
            if ants_at_pos[p] and len(ants_at_pos[p]) > 1:
                for a in ants_at_pos[p]:
                    if a in ants:
                        ants[a] = -1 * ants[a]        

                        


    print('Case #{}: {}'.format(t+1,' '.join([str(a) for a in ans])))