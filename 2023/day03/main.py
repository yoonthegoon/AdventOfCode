import re


with open('input.txt') as f:
    engine_schematic = f.read().splitlines()


def part1():
    numbers_indices = {}
    symbols_indices = {}
    for i, line in enumerate(engine_schematic):
        line_numbers_indices = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
        line_symbols_indices = [match.start() for match in re.finditer(r'[^\d.]', line)]
        numbers_indices[i] = line_numbers_indices
        symbols_indices[i] = line_symbols_indices

    part_numbers = []
    for i, _ in enumerate(engine_schematic):
        for j in range(-1, 2):
            for symbol_index in symbols_indices[i]:
                if i + j < 0 or i + j >= len(engine_schematic):
                    continue

                for number_indices in numbers_indices[i + j]:
                    if symbol_index in range(number_indices[0] - 1, number_indices[1] + 1):
                        part_numbers.append(int(engine_schematic[i + j][number_indices[0]:number_indices[1]]))

    print(sum(part_numbers))


def part2():
    numbers_indices = {}
    gears_indices = {}
    for i, line in enumerate(engine_schematic):
        line_numbers_indices = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
        line_symbols_indices = [match.start() for match in re.finditer(r'\*', line)]
        numbers_indices[i] = line_numbers_indices
        gears_indices[i] = line_symbols_indices

    gear_ratios = []
    for i, _ in enumerate(engine_schematic):
        for gear_index in gears_indices[i]:
            numbers = []
            for j in range(-1, 2):
                if i + j < 0 or i + j >= len(engine_schematic):
                    continue

                for number_indices in numbers_indices[i + j]:
                    if gear_index in range(number_indices[0] - 1, number_indices[1] + 1):
                        numbers.append(int(engine_schematic[i + j][number_indices[0]:number_indices[1]]))
                        if len(numbers) > 2:
                            break
                else:
                    continue
            else:
                if len(numbers) == 2:
                    gear_ratios.append(numbers[0] * numbers[1])

    print(sum(gear_ratios))


if __name__ == '__main__':
    part1()
    part2()
