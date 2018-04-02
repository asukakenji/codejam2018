# code jam: Practice Session 2018: Q2: Senate Evacuation

# Limits
# 1 <= T <= 50.
# No party will have an absolute majority before the start of the evacuation.
# 1 <= P[i] <= 1000, for all i.
# Time limit: 30 seconds per test set.
# Memory limit: 1GB.

# Test set 1 (Visible)
# 2 <= N <= 3.
# sum of all Pi <= 9.

# Test set 2 (Hidden)
# 2 <= N <= 26.
# sum of all Pi <= 1000.

def read_int():
    return int(raw_input())

def read_int_n():
    return map(int, raw_input().split())

def resort(mylist, n):
    i = 0
    j = 1
    while j < n:
        if mylist[i][0] < mylist[j][0]:
            mylist[i], mylist[j] = mylist[j], mylist[i]
            i += 1
            j += 1
        else:
            break

t = read_int() # 1 <= T <= 50.
tt = 1
while tt <= t:
    n = read_int()
    p = read_int_n() # 1 <= P[i] <= 1000, for all i.
    sum_of_p_i = 0
    for p_i in p:
        sum_of_p_i += p_i
    p = [(pi, chr(65 + i)) for i, pi in enumerate(p)]
    p = sorted(p, key=lambda t: t[0], reverse=True)
    ss = []
    while p[0][0] != 0:
        s = ''
        # Evacuation the 1st senate
        p[0] = (p[0][0] - 1, p[0][1])
        sum_of_p_i -= 1
        s += p[0][1]
        resort(p, n)
        if p[0][0] != 0:
            if sum_of_p_i == 1 or (sum_of_p_i != 1 and float(p[1][0]) / (sum_of_p_i - 1) <= 0.5):
                p[0] = (p[0][0] - 1, p[0][1])
                sum_of_p_i -= 1
                s += p[0][1]
                resort(p, n)
        ss.append(s)
    print 'Case #%d: %s' % (tt, ' '.join(ss))
    tt += 1
