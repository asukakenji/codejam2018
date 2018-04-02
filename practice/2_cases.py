import sys

# def gen2(sum_of_p_i):
#     a = 1
#     half_sum = sum_of_p_i >> 1
#     while a <= half_sum:
#         b = sum_of_p_i - a
#         if b >= a and b <= half_sum:
#             print a, b
#         a += 1
#
# def gen3(sum_of_p_i):
#     a = 1
#     half_sum = sum_of_p_i >> 1
#     while a <= half_sum:
#         b = a
#         while b <= half_sum and b <= sum_of_p_i - a:
#             c = sum_of_p_i - a - b
#             if c >= b and c <= half_sum:
#                 print a, b, c
#             b += 1
#         a += 1
#
# def gen4(sum_of_p_i):
#     a = 1
#     half_sum = sum_of_p_i >> 1
#     while a <= half_sum:
#         b = a
#         while b <= half_sum and b <= sum_of_p_i - a:
#             c = b
#             while c <= half_sum and c <= sum_of_p_i - a - b:
#                 d = sum_of_p_i - a - b - c
#                 if d >= c and d <= half_sum:
#                     print a, b, c, d
#                 c += 1
#             b += 1
#         a += 1

def genn_impl(result, list, n_minus_one, half, i, sum):
    if i == n_minus_one:
        list[i] = sum
        if list[i] >= list[i-1] and list[i] <= half:
            result.append(list[:])
    else:
        if i == 0:
            v = 1
        else:
            v = list[i-1]
        while v <= half and v <= sum:
            list[i] = v
            genn_impl(result, list, n_minus_one, half, i + 1, sum - v)
            v += 1

def genn(n, sum_of_p_i):
    result = []
    list = [0] * n
    genn_impl(result, list, n - 1, sum_of_p_i >> 1, 0, sum_of_p_i)
    return result

n = int(sys.argv[1])
sum_of_p_i = int(sys.argv[2])
result = genn(n, sum_of_p_i)
t = len(result)
print t
for list in result:
    print n
    print '%s' % ' '.join(map(str, list))
