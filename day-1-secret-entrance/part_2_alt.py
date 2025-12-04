max_ticks = 100

# input_lines = open('example-input.txt').read().split('\n')
input_lines = open('input.txt').read().split('\n')


# This is the Mathy Solution
def tick(curr_position, move_instruction):
    num_zeros_ticked_to = 0
    new_position = 0

    started_at_zero = curr_position == 0

    if curr_position == 0:
        num_zeros_ticked_to -= 1

    letter, ticks = move_instruction[:1], int(move_instruction[1:])
    if letter == 'L':
        rotations = abs((curr_position - ticks) // max_ticks)
        curr_position = (curr_position - ticks) % max_ticks
        ended_at_zero = curr_position == 0

        if started_at_zero:
            rotations = max(0, rotations - 1)

        if letter == 'L' and ended_at_zero:
            rotations += 1
    elif letter == 'R':
        rotations = (curr_position + ticks) // max_ticks
        curr_position = (curr_position + ticks) % max_ticks

    return curr_position, rotations


test_cases = [
    [50, 'L68', 82, 1],
    [82, 'L30', 52, 0],
    [52, 'R48', 0, 1],
    [0, 'L5', 95, 0],
    [95, 'R60', 55, 1],
    [55, 'L55', 0, 1],
    [0, 'L1', 99, 0],
    [99, 'L99', 0, 1],
    [0, 'R14', 14, 0],
    [14, 'L82', 32, 1],
    [0, 'R874', 74, 8],  ## First mismatch from brute force
]

test_passed = True
for curr_position, instruction, e_next_position, e_rotations in test_cases:
    a_next_position, a_rotations = tick(curr_position, instruction)

    if not all([
        a_next_position == e_next_position,
        a_rotations == e_rotations
    ]):
        print(f'BAD  = {curr_position, instruction} = {a_next_position, a_rotations}')
        test_passed = False

if not test_passed:
    print('TESTS FAILED!')
    exit(1)


class BruteForceSolution:
    def __init__(self, starting_position=50, max_ticks=100):
        self._pos = starting_position
        self.ticks = list(range(max_ticks))

    def tick(self, instruction):
        num_zero_hits = 0
        letter, ticks = instruction[:1], int(instruction[1:])
        if letter == 'L':
            for i in range(ticks):
                self._pos -= 1
                if self._pos < 0:
                    self._pos = 99
                if self._pos == 0:
                    num_zero_hits += 1
        else:
            for i in range(ticks):
                self._pos += 1
                if self._pos > 99:
                    self._pos = 0
                    num_zero_hits += 1

        return num_zero_hits

    @property
    def curr_position(self):
        return self._pos


answer = 0
curr_position = 50
brute_force_answer = 0
brute_force_solution = BruteForceSolution()
for instruction in input_lines:
    brute_force_rotations = 0
    prev_pos = curr_position
    b_prev_pos = brute_force_solution.curr_position
    curr_position, rotations = tick(curr_position, instruction)
    answer += rotations
    brute_force_rotations += brute_force_solution.tick(instruction)

    if brute_force_rotations != rotations:
        print(
            f'BAD - start={prev_pos, b_prev_pos}, inst={instruction} -> end={curr_position}, rotations={rotations} || end={brute_force_solution.curr_position}, rotations={brute_force_rotations}')
    brute_force_answer += brute_force_rotations

print(f'Answer: {answer}')
print(f'Answer: {brute_force_answer}')
