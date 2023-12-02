import re


with open("input.txt") as f:
    calibration_document = f.read().splitlines()


def part1():
    calibration_values = []
    for line in calibration_document:
        digits = re.findall(r'\d', line)
        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)

    answer = sum(calibration_values)

    print(answer)


def part2():
    digit_map = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8',
        'nine': 'n9e'
    }
    calibration_values = []
    for line in calibration_document:
        for digit in digit_map:
            line = line.replace(digit, digit_map[digit])

        digits = re.findall(r'\d', line)
        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)

    answer = sum(calibration_values)

    print(answer)


if __name__ == '__main__':
    part1()
    part2()
