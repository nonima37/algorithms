package main

import (
	"fmt"
	"math"
	"regexp"
	"strconv"
)

var curToken int = 0
var tokens []string
var lookAhead string

func lexan(inputString string) {
	i := 0

	for i < len(inputString) {
		c := string(inputString[i])
		_, err := strconv.ParseFloat(c, 8)
		token := ""

		if err == nil {
			re, _ := regexp.Compile("[.0-9]+")
			token = re.FindString(inputString[i:])
			i += len(token)
		} else {
			token = c
			i++
		}
		tokens = append(tokens, token)
	}
	lookAhead = tokens[curToken]
}

func expr() float64 {
	result := term()
	for {
		if lookAhead == "+" {
			match()
			result += term()
		} else if lookAhead == "-" {
			match()
			result -= term()
		} else {
			break
		}
	}
	return result
}

func term() float64 {
	result := factor()
	for {
		if lookAhead == "*" {
			match()
			result *= factor()
		} else if lookAhead == "/" {
			match()
			result /= factor()
		} else {
			break
		}
	}
	return result
}

func factor() float64 {
	result := base()
	if lookAhead == "^" {
		match()
		result = math.Pow(result, factor())
	}
	return result
}

func base() float64 {
	result := float64(0)
	intValue, err := strconv.ParseFloat(lookAhead, 8)
	if lookAhead == "(" {
		// doesn't work
		match()
		result = expr()
		// closing the parantheses
		match()
	} else if err == nil {
		result = intValue
		match()
	} else if lookAhead == "-" {
		match()
		result = -1 * base()
	}
	return result
}

func match() {
	if curToken < len(tokens)-1 {
		curToken++
		lookAhead = tokens[curToken]
	}
}

func main() {
	lexan("1+3/2")
	fmt.Println(expr())
}
