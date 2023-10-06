package utils

import (
    "bufio"
    "os"
    "strings"
)

func ReadInput() string {
    input, err := os.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }
    return string(input)
}

func ReadInputLines() []string {
    input := ReadInput()
    scanner := bufio.NewScanner(strings.NewReader(input))
    var lines []string
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines
}

