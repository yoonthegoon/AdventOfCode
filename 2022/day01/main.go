package main

import (
    "fmt"
    "strconv"

    "github.com/yoonthegoon/AdventOfCode/utils"
)

func main() {
    input := utils.ReadInputLines()
    part1(input)
}

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

