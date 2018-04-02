# code jam: Practice Session 2018: Q3: Steed 2: Cruise Control

# Limits
# 1 <= T <= 100.
# 0 < K[i] < D <= 10**9, for all i.
# K[i] != K[j], for all i != j. (No two horses start in the same position.)
# 1 <= S[i] <= 10000.
# Time limit: 10 seconds per test set.
# Memory limit: 1GB.
#
# Test set 1 (Visible)
# 1 <= N <= 2.
#
# Test set 2 (Hidden)
# 1 <= N <= 1000.

def read_int():
    return int(raw_input())

def read_int_n():
    return map(int, raw_input().split())

Infinity = float("inf")

T = read_int()
x = 1
while x <= T:
    D, N = read_int_n()
    KS = []
    i = 0
    while i < N:
        K, S = read_int_n()
        KS.append((K, S))
        i += 1
    KS = sorted(KS, key=lambda tuple: tuple[0])
    time = 0
    while len(KS) != 1:
        t_min = Infinity
        s_min = 0
        i_min = 0
        for i in xrange(0, len(KS) - 1):
            j = i + 1
            if KS[i][1] == KS[j][1]: # S[i] == S[j]
                # Since the their speeds are the same, the horses will never merge
                continue
            else:
                t = float(KS[j][0] - KS[i][0]) / (KS[i][1] - KS[j][1]) # K[j] - K[i] / (S[i] - S[j])
                if t < 0:
                    # Since the horse at the back is slower, the horses will never meet (merge)
                    continue
                elif t == 0:
                    # Since the horses share the same position, they will merge immediately
                    t_min = 0
                    i_min = i
                    break
                else: # t > 0
                    if KS[i][0] + KS[i][1] * t > D:
                        # Since the horses will meet after the goal, they will never merge
                        continue
                    else:
                        if t < t_min:
                            # The horses will meet before the goal, the soonest pair will merge
                            t_min = t
                            s_min = KS[j][1]
                            i_min = i
        if t_min == Infinity:
            break
        time += t_min
        del KS[i_min+1]
        for i in xrange(len(KS)):
            if i != i_min:
                KS[i] = (KS[i][0] + KS[i][1] * t_min, KS[i][1])
            else:
                KS[i] = (KS[i][0] + KS[i][1] * t_min, s_min)
    time += float(D - KS[0][0]) / KS[0][1]
    y = D / time
    print 'Case #%d: %f' % (x, y)
    x += 1
