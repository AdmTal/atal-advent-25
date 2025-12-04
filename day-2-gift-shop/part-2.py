# input_line = open('./example-input.txt').read().split('\n')[0]
input_line = open('./input.txt').read().split('\n')[0]

id_ranges = input_line.split(',')


def is_valid_id(id):
    id_str = str(id)
    id_str_n = len(id_str)

    if id_str_n == 1:
        return True

    # We need to split the string into parts ...
    # 2, 3, 4, 5 ... N
    for i in range(1, id_str_n):
        # If not evenly divisible by i, skip
        if id_str_n % i != 0:
            continue

        # Evenly Divide
        parts = []
        start = 0
        while start < id_str_n:
            parts.append(id_str[start:start + i])
            start += i
        if len(set(parts)) == 1:
            return False

    return True


answer = 0
for id_range in id_ranges:
    first, last = [int(i) for i in id_range.split('-')]
    for i in range(first, last + 1):
        if not is_valid_id(i):
            answer += i

print(answer)
