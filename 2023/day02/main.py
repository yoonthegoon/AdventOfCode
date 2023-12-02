import re


with open('input.txt') as f:
    games = f.readlines()


def part1():
    id_sum = 0
    for game in games:
        game_id = int(re.search(r'(?<=Game )\d+(?=:)', game).group())
        for game_set in game.split(';'):
            reds = map(int, re.findall(r'\d+(?= red)', game_set))
            greens = map(int, re.findall(r'\d+(?= green)', game_set))
            blues = map(int, re.findall(r'\d+(?= blue)', game_set))
            if sum(reds) > 12 or sum(greens) > 13 or sum(blues) > 14:
                break
        else:
            id_sum += game_id

    print(id_sum)


def part2():
    power_sum = 0
    for game in games:
        max_red, max_green, max_blue = (0,) * 3
        for game_set in game.split(';'):
            reds = map(int, re.findall(r'\d+(?= red)', game_set))
            greens = map(int, re.findall(r'\d+(?= green)', game_set))
            blues = map(int, re.findall(r'\d+(?= blue)', game_set))
            max_red = max(max_red, sum(reds))
            max_green = max(max_green, sum(greens))
            max_blue = max(max_blue, sum(blues))

        power_sum += max_red * max_green * max_blue

    print(power_sum)


if __name__ == '__main__':
    part1()
    part2()
