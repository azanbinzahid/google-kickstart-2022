T = int(input())

# recursive
def solve(D, start, end, last_served=0):

    if start == end:
        return 1 if D[start] >= last_served else 0 
    
    a = 1 if D[start] >= last_served else 0
    b = 1 if D[end] >= last_served else 0
    
    return max(
        a+solve(D, start+1, end, max(D[start], last_served)),
        b+solve(D, start, end-1, max(D[end], last_served))
    )

# didn't work 
# def solve_iterative(D):

#     start = 0
#     end = len(D)-1
#     last_served = 0
#     ans = 0

#     while start <= end:

#         if D[start] < D[end] and D[start] >= last_served:
#             last_served = max(D[start], last_served)
#             start += 1
#             ans += 1
        
#         elif D[start] >= D[end] and D[end] >= last_served:
#             last_served = max(D[end], last_served)
#             end -= 1
#             ans+=1

#         else:
#             if D[start] < D[end]:
#                 start += 1
#                 last_served = max(D[start], last_served)
#             else:
#                 end -= 1
#                 last_served = max(D[end], last_served)

#     return ans

for t in range(T):
    N = int(input())
    D = list(map(int, input().split()))
    ans = solve(D, start=0, end = len(D)-1)
    # ans = solve_iterative(D)
    print('Case #{}: {}'.format(t+1,ans))