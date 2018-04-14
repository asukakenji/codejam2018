# code jam: Qualification Round 2018: Problem A. Saving The Universe Again

def get_damage(P):
    damage = 0
    strength = 1
    for c in P:
        if c == 'C':
            strength <<= 1
        elif c == 'S':
            damage += strength
        else:
            raise Exception
    return damage

def change_code(P):
    index = P.rindex('CS')
    return P[:index] + 'SC' + P[index+2:]

T = int(raw_input())
x = 1
while x <= T:
    D, P = raw_input().split()
    D = int(D)
    min_damage = P.count('S')
    if min_damage > D:
        print 'Case #{}: IMPOSSIBLE'.format(x)
        x += 1
        continue
    y = 0
    while True:
        damage = get_damage(P)
        if damage <= D:
            break
        P = change_code(P)
        y += 1
    print 'Case #{}: {}'.format(x, y)
    x += 1
