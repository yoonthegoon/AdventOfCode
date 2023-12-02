# Day 1 - 2022

## Part 1

We are given a `calibration document` which consists of lines of text.
Each line contains a `calibration value` which can be found by combining the first digit and the last digit of the line.
For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

The `calibration values` of these four lines are `12`, `38`, `15`, and `77`.
The sum of these values is `142`.
We have to find the sum of all the calibration values.

Before starting, I read my puzzle input.
I also import the `re` module to help me find the digits in each line.

```python
import re

with open("input.txt") as f:
    calibration_document = f.read().splitlines()
```

I create an empty list to store the calibration values.
I then iterate through each line in the calibration document.
I use `re.findall` to find all the digits in the line.
I then combine the first digit and the last digit to create the calibration value.
I append the calibration value to the list of calibration values.

```python
def part1():
    calibration_values = []
    for line in calibration_document:
        digits = re.findall(r'\d', line)
        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)

    answer = sum(calibration_values)

    print(answer)
```

The answer is the sum of all the calibration values, which is `54697` for my input.

## Part 2

The second part is a little trickier.
My initial solution felt really clunky, but what I have now feels more like an elegant hack.

Rather than concerning ourselves with the first and last digits of each line exclusively,
we now have to also consider some of the digits are actually spelled out with letters.
For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

The `calibration values` are 29, 83, 13, 24, 42, 14, and 76.
A naive approach would be to have a dictionary like the following:

```python
digit_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
```

And for each line, we would replace the spelled out digits with their numerical counterparts as follows:

```python
for line in calibration_document:
    for digit in digit_map:
        line = line.replace(digit, digit_map[digit])
```

However, look at the second line in the example above.
Using this approach, we would end up with `eight23` instead of `823`, resulting in a `calibration value` of `23` instead of `83`.
We need to be more clever.

I decided to use the following dictionary instead:

```python
digit_map = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}
```

This way, we can replace the spelled out digits with their numerical counterparts without worrying about replacing parts of other spelled out digits.
So the second line would now become `e8t2ot3e`.
The `2` doesn't belong, but because it cannot be at the beginning or end of the line, we can safely ignore it.
So we end up with the correct `calibration value` of `83`.
Here's my solution:

```python
def part2():
    digit_map = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
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
```

You can see that besides the dictionary, the only difference between this solution and the previous one is the addition of the `for` loop that replaces the spelled out digits with their numerical counterparts.
The solution for part 2 is `54885` for my input.
