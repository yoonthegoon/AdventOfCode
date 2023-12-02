import re
from math import prod


with open('input.txt') as f:
    games = f.readlines()


def part1():
    colors = {'red': 12, 'green': 13, 'blue': 14}
    id_sum = 0
    for game in games:
        game_id = int(re.search(r'(?<=Game )\d+(?=:)', game).group())
        for game_set in game.split(';'):
            cubes = {color: map(int, re.findall(rf'\d+(?= {color})', game_set)) for color in colors}
            if any(sum(cubes[color]) > colors[color] for color in colors):
                break
        else:
            id_sum += game_id

    print(id_sum)


def part2():
    power_sum = 0
    for game in games:
        maxes = {'red': 0, 'green': 0, 'blue': 0}
        for game_set in game.split(';'):
            cubes = {color: map(int, re.findall(rf'\d+(?= {color})', game_set)) for color in maxes}
            for color in maxes:
                maxes[color] = max(maxes[color], sum(cubes[color]))

        power_sum += prod(maxes.values())

    print(power_sum)


if __name__ == '__main__':
    part1()
    part2()
