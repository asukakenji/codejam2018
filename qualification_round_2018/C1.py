# code jam: Qualification Round 2018: Problem C. Go, Gopher!

from __future__ import print_function
import sys
import collections

def find_IJ(IJ_set, f):
    l = []
    I = 2
    while I <= 3:
        J = 2
        while J <= 4:
            score = 0
            for dI in [-1, 0, 1]:
                II = I + dI
                for dJ in [-1, 0, 1]:
                    JJ = J + dJ
                    if (II, JJ) not in IJ_set:
                        score += 1
            l.append((score, (I, J)))
            J += 1
        I += 1
    l.sort(reverse=True)
    print(l, file=f)
    return l[0][1]

with open('C.out', 'w') as f:
    T = int(raw_input())
    x = 1
    while x <= T:
        WH_list = []
        A = int(raw_input())
        # if A == 20:
        #     WH_list = [(1,20),(2,10),(4,5),(5,4),(10,2),(20,1)]
        # elif A == 200:
        #     WH_list = [(1,200),(2,100),(4,50),(5,40),(8,25),(10,20),(20,10),(25,8),(40,5),(50,4),(100,2),(200,1)]
        # else:
        #     raise Exception('A is not 20 or 200')
        IJ_set = set()
        i = 0
        is_prepared = False
        I, J = 0, 0
        while i < 1000:
            print('Iteration {}'.format(i), file=f)
            print(IJ_set, file=f)
            if not is_prepared:
                I, J = find_IJ(IJ_set, f)
            print(I, J, file=f, end=' ')
            print(I, J) # 2 <= I, J <= 999
            sys.stdout.flush()
            I_dash, J_dash = map(int, raw_input().split())
            print('=>', I_dash, J_dash, file=f)
            print(file=f)
            if I_dash == -1 or J_dash == -1:
                raise Exception('Format Error: ' + str(I) + ' ' + str(J))
            if I_dash == 0 and J_dash == 0:
                break
            # WH_list = filter(lambda WH: I_dash <= WH[0] and J_dash <= WH[1], WH_list)
            if (I_dash, J_dash) in IJ_set:
                is_prepared = True
            else:
                IJ_set.add((I_dash, J_dash))
                is_prepared = False
            i += 1
        else:
            raise Exception('Not Solved')
        x += 1
