def sum_list(x):
    if len(x) == 1:
        return x[0]
    return x[0] + sum_list(x[1:])


print(sum_list([1, 2, 3, 4, 5, ]))


def draw(n):
    if n == 0:
        return
    print('*' * n)
    draw(n - 1)
    print('#' * n)


draw(5)


def gen01(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        gen01(index + 1, vector)


n = 4
vector = [0] * n


def print_bits(bits_count, index=0, number=''):
    if bits_count == index:
        print(number)
        return
    for digit in list('01'):
        print_bits(bits_count, index + 1, number + digit)


print_bits(int(input()))


def print_bits2(index, vector):
    if index >= len(vector):
        print("".join([str(x) for x in vector]))
        return
    for n in range(2):
        vector[index] = n
        print_bits2(index + 1, vector)


vector = ['s'] * 3
print_bits2(0, vector)

