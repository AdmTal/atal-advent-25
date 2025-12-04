# input_line = open('./example-input.txt').read().split('\n')[0]
input_line = open('./input.txt').read().split('\n')[0]

id_ranges = input_line.split(',')


def is_valid_id(id):
    id_str = str(id)
    id_str_n = len(id_str)

    if len(id_str) % 2 != 0:
        # Odd length always good
        return True

    midpoint = id_str_n // 2
    first_half, second_half = id_str[:midpoint], id_str[midpoint:]

    return first_half != second_half

answer = 0
for id_range in id_ranges:
    first, last = [int(i) for i in id_range.split('-')]
    for i in range(first, last+1):
        if not is_valid_id(i):
            answer += i

print(answer)
