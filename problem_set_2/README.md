# Problem Set 2: Valid Parentheses

## Problem Description
Given a string consisting of parentheses, curly braces, and square brackets, determine if the string is valid. A string is valid if each opening bracket has a corresponding closing bracket of the same type, and they are correctly nested.

## Solution Overview
 - **Stack Method** - I leveraged the stack method to solve this problem.
 - If the character of the input is an opening bracket, then it is pushed on the stack.
 - While if the character is a closing bracket, we then pop the top of the stack and check if the popped opening bracket matches the closing bracket. In case of an empty stack, it is immediately results to false since there's no corresponding opening bracket.
 - After iterating all the characters, if the stack is empty, then the string is valid.

## Instructions to Run the Code
 - Just run the code and it will show the output for the initial sample input.
 - You can check other test cases by changing the argument for the is_valid function *(I made valid and invalid inputs to test different scenarios)*.