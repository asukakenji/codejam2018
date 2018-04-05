# code jam: Qualification Round 2017: Problem B. Tidy Numbers

T = int(raw_input())
x = 1
while x <= T:
    N = raw_input()
    y = map(int, N)
    i, j, limit = 0, 0, len(y) - 1
    while i < limit:
        if y[i] > y[i+1]:
            y[i] -= 1
            for k in range(i+1, len(y)):
                y[k] = 9
            j = i - 1
            while j >= 0:
                if y[j] > y[j+1]:
                    y[j] -= 1
                    y[j+1] = 9
                else:
                    break
                j -= 1
            break
        i += 1
    print 'Case #{}: {}'.format(x, ''.join(map(str, y)).lstrip('0'))
    x += 1
