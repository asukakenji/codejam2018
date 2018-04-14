# code jam: Qualification Round 2018: Problem C. Go, Gopher!

import sys
import collections

def find_IJ(WH_list, IJ_set):
    d = collections.defaultdict(lambda: 0)
    # Positive Score
    for WH in WH_list:
        W, H = WH
        I = 1
        while I <= W:
            J = 1
            while J <= H:
                if (I, J) not in IJ_set:
                    # print I, J, 'not in IJ_set'
                    for dI in [-1, 0, 1]:
                        for dJ in [-1, 0, 1]:
                            II, JJ = I+dI, J+dJ
                            # print II, JJ
                            if II >= 2 and JJ >= 2:
                                d[(II,JJ)] += 1
                J += 1
            I += 1
    # Negative Score
    for IJ in d:
        I, J = IJ
        for WH in WH_list:
            W, H = WH
            for dI in [-1, 0, 1]:
                for dJ in [-1, 0, 1]:
                    II, JJ = I+dI, J+dJ
                    if II > W or JJ > H:
                        d[IJ] -= 1
    # Sort and Find Highest
    l = [(d[IJ], IJ) for IJ in d]
    l.sort(key=lambda x: x[0], reverse=True)
    return l[0][1]

T = int(raw_input())
x = 1
while x <= T:
    WH_list = []
    A = int(raw_input())
    if A == 20:
        WH_list = [(1,20),(2,10),(4,5),(5,4),(10,2),(20,1)]
    elif A == 200:
        WH_list = [(1,200),(2,100),(4,50),(5,40),(8,25),(10,20),(20,10),(25,8),(40,5),(50,4),(100,2),(200,1)]
    else:
        raise Exception('A is not 20 or 200')
    IJ_set = set()
    i = 0
    is_prepared = False
    I, J = 0, 0
    while i < 1000:
        if not is_prepared:
            I, J = find_IJ(WH_list, IJ_set)
        print I, J # 2 <= I, J <= 999
        sys.stdout.flush()
        I_dash, J_dash = map(int, raw_input().split())
        if I_dash == -1 or J_dash == -1:
            raise Exception('Format Error: ' + str(I) + ' ' + str(J))
        if I_dash == 0 and J_dash == 0:
            break
        WH_list = filter(lambda WH: I_dash <= WH[0] and J_dash <= WH[1], WH_list)
        if (I_dash, J_dash) in IJ_set:
            is_prepared = True
        else:
            IJ_set.add((I_dash, J_dash))
            is_prepared = False
        i += 1
    else:
        raise Exception('Not Solved')
    x += 1
