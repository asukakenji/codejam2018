# code jam: Qualification Round 2017: Problem C. Bathroom Stalls

def read_int():
    return int(raw_input())

def read_int_n():
    return map(int, raw_input().split())

def get_y_z(n, k):
    if k == 1:
        if n & 1 == 0:
            # Even Number
            return n >> 1, (n >> 1) - 1
        else:
            # Odd Number
            return n >> 1, n >> 1
    else:
        if n & 1 == 0:
            # Even Number
            if k & 1 == 0:
                # Even Number
                return get_y_z(n >> 1, k >> 1)
            else:
                # Odd Number
                return get_y_z((n >> 1) - 1, k >> 1)
        else:
            # Odd Number
            return get_y_z(n >> 1, k >> 1)

T = read_int()
x = 1
while x <= T:
    N, K = read_int_n()
    y, z = get_y_z(N, K)
    print 'Case #{}: {} {}'.format(x, y, z)
    x += 1
