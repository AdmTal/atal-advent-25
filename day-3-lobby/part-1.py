input_items = open('./example-input.txt').read().split('\n')


# input_items = open('./input.txt').read().split('\n')

def get_bank_max_voltage(bank, num_batteries=2):
    bank_n = len(bank)
    largest_ordered_digits = []

    for number_str in bank[:-1]:
        number = int(number_str)
        if not largest_ordered_digits or len(largest_ordered_digits) < num_batteries:
            largest_ordered_digits.append(number)
            continue
        for idx, lod in enumerate(largest_ordered_digits):
            if number > lod:
                largest_ordered_digits[idx] = number

    return int(''.join([str(i) for i in largest_ordered_digits]))


answer = 0
for bank in input_items:
    x = get_bank_max_voltage(bank)
    print(f'{bank} => {x}')
    answer += get_bank_max_voltage(bank)

print(f'Answer: {answer}')
