# code jam: Round 1A 2018: Problem A. Waffle Choppers

def cut(B, R, C):
    newB = []
    if R == 0:
        for Bi in B:
            ltSet = set()
            geSet = set()
            for chocolate in Bi:
                if chocolate[1] < C:
                    ltSet.add(chocolate)
                else:
                    geSet.add(chocolate)
            newB.append(ltSet)
            newB.append(geSet)
    else:
        for Bi in B:
            ltSet = set()
            geSet = set()
            for chocolate in Bi:
                if chocolate[0] < R:
                    ltSet.add(chocolate)
                else:
                    geSet.add(chocolate)
            newB.append(ltSet)
            newB.append(geSet)
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
    for r in range(R - 1):
        B0 = cut(B, r + 1, 0)
        if check(B0):
            for c in range(C - 1):
                B1 = cut(B0, 0, c + 1)
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
