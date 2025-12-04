max_ticks = 100
curr_position = 50

input_lines = open('example-input.txt').read().split('\n')
# input_lines = open('input.txt').read().split('\n')

num_zeros = 0
for line in input_lines:
    letter, num = line[:1], int(line[1:])
    prev_position = curr_position
    if letter == 'L':
        curr_position = (curr_position - num) % max_ticks
        rotations = abs((prev_position - num) // max_ticks)
        if prev_position == 0 and rotations:
            rotations -= 1
    elif letter == 'R':
        curr_position = (curr_position + num) % max_ticks
        rotations = (prev_position + num) // max_ticks
        if prev_position == 0 and rotations:
            rotations -= 1
    print(f'{line} - from {prev_position} to {curr_position} - rotations = {rotations}')
    num_zeros += rotations

print(f'Answer: {num_zeros}')

# PROBLEM - L55 - from 55 to 0 - rotations = 0