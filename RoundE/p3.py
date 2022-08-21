T = int(input())
def isPalindrome(Str):
 
    Len = len(Str)
 
    # single character is always palindrome
    if (Len == 1):
        return True
 
    # pointing to first character
    ptr1 = 0
 
    # pointing to last character
    ptr2 = Len - 1
 
    while (ptr2 > ptr1):
 
        if (Str[ptr1] != Str[ptr2]):
            return False
        ptr1 += 1
        ptr2 -= 1
 
    return True
def solve(p):
    i = 1
    p_rev = p[::-1]
    check = p+p_rev[:i]
    while(not isPalindrome(check)):
        i+=1
        check = p+p_rev[:i]

    return p_rev[:i]



for t in range(T):

    _ = input()
    w = input()

    print('Case #{}: {}'.format(t+1, solve(w)))

# Test Case 1 Pass
