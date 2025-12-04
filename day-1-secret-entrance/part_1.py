max_ticks = 100
curr_position = 50

# input_lines = open('example-input.txt').read().split('\n')
input_lines = open('input.txt').read().split('\n')

num_zeros = 0
for line in input_lines:
    letter, num = line[:1], int(line[1:])
    if letter == 'L':
        curr_position = (curr_position - num) % max_ticks
    elif letter == 'R':
        curr_position = (curr_position + num) % max_ticks
    num_zeros += bool(curr_position == 0)

print(f'Answer: {num_zeros}')
