# Day 1 - 2022

## Part 1

I have a function [ReadInputLines](https://github.com/yoonthegoon/AdventOfCode/blob/main/utils/utils.go)
that does exactly as it says. It returns `[]string`, a slice of string where
each element of the slice is a line from [input.txt](./input.txt).

The firt thing I do is initialize a running total for each individual elf'
calorie count and the maximum total (what we're looking for).

```go
total := 0
maxTotal := 0
```

Next, I read each line from my input and convert it to an integer.

```go
// import "strconv"

maxTotal := 0
for _, line := range input {
    c, err := strconv.Atoi(line)
    // i'm not done yet
}
```

I want to add `c` (calories) to the total, but clear the total and compare to
the max total if I come accross an empty line.

```go
c, err := strconv.Atoi(line)
if c == 0 {
    if total > maxTotal {
        maxTotal = total
    }
    total = 0
    continue
}
total += c
```

All together, it comes out to this:

```go
func part1(input []string) {
    total := 0
    maxTotal := 0
    for _, line := range input {
        c, _ := strconv.Atoi(line)
        if c == 0 {
            if total > maxTotal {
                maxTotal = total
            }
            total = 0
            continue
        }
        total += c
    }
    fmt.Println(maxTotal)
}
```

## Part 2

