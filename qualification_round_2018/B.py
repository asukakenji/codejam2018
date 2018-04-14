# code jam: Qualification Round 2018: Problem B. Trouble Sort

def trouble_sort(L):
    done = False
    limit = len(L) - 2
    while not done:
        done = True
        i = 0
        while i < limit:
            if L[i] > L[i+2]:
                done = False
                L[i], L[i+2] = L[i+2], L[i]
            i += 1

def check_list(L):
    i = 0
    limit = len(L) - 1
    while i < limit:
        if L[i] > L[i+1]:
            return i
        i += 1
    return -1

T = int(raw_input())
x = 1
while x <= T:
    N = int(raw_input())
    V_list = map(int, raw_input().split())
    trouble_sort(V_list)
    index = check_list(V_list)
    if index == -1:
        y = 'OK'
    else:
        y = index
    print 'Case #{}: {}'.format(x, y)
    x += 1
