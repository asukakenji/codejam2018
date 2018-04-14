# code jam: Round 1A 2018: Problem A. Waffle Choppers

def possible_cuts_impl(RC, HV, A, n, x):
    if n == HV:
        yield A[:]
    else:
        for i in range(x, RC-1):
            A[n] = i+1
            for t in possible_cuts_impl(RC, HV, A, n+1, i+1):
                yield t

def possible_cuts(RC, HV):
    for t in possible_cuts_impl(RC, HV, [0]*HV, 0, 0):
        yield t

def cut(B, HV, RC):
    newB = []
    if HV == 'H':
        # R = RC
        for Bi in B:
            ltSet = set()
            geSet = set()
            for chocolate in Bi:
                if chocolate[0] < RC:
                    ltSet.add(chocolate)
                else:
                    geSet.add(chocolate)
            newB.append(ltSet)
            newB.append(geSet)
    else:
        # C = RC
        for Bi in B:
            ltSet = set()
            geSet = set()
            for chocolate in Bi:
                if chocolate[1] < RC:
                    ltSet.add(chocolate)
                else:
                    geSet.add(chocolate)
            newB.append(ltSet)
            newB.append(geSet)
    return newB

def mcut(B, HV, cuts):
    newB = [set() for i in xrange((len(cuts)+1) * len(B))]
    if HV == 'H':
        for i, Bi in enumerate(B):
            for chocolate in Bi:
                for j, c in enumerate(cuts):
                    if chocolate[0] < c:
                        newB[i * len(B) + j].add(chocolate)
                        break
                else:
                    newB[i * len(B) + len(cuts)].add(chocolate)
    else:
        for i, Bi in enumerate(B):
            for chocolate in Bi:
                for j, c in enumerate(cuts):
                    if chocolate[1] < c:
                        newB[i * len(B) + j].add(chocolate)
                        break
                else:
                    newB[i * len(B) + len(cuts)].add(chocolate)
    return newB

def check(B):
    count = len(B[0])
    for Bi in B:
        if len(Bi) != count:
            return False
    return True

def solve(R, C, H, V, D, B):
    if len(B[0]) % D != 0:
        return False
    for h_cuts in possible_cuts(R, H):
        B0 = mcut(B, 'H', h_cuts)
        if check(B0):
            for v_cuts in possible_cuts(C, V):
                B1 = mcut(B0, 'V', v_cuts)
                if check(B1):
                    return True
    return False

T = int(raw_input())
x = 1
while x <= T:
    R, C, H, V = map(int, raw_input().split())
    D = (H + 1) * (V + 1)
    B0 = set()
    for r in range(R):
        row = raw_input()
        for c, ch in enumerate(row):
            if ch == '@':
                B0.add((r, c))
    if solve(R, C, H, V, D, [B0]):
        y = 'POSSIBLE'
    else:
        y = 'IMPOSSIBLE'
    print 'Case #{}: {}'.format(x, y)
    x += 1
