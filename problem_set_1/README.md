# Problem Set 1: Palindrome Pairs

## Problem Description
Given a list of unique words, find all pairs of distinct indices (i, j) such that the concatenation of words[i] and words[j] forms a palindrome.

## Solution Overview
 - **Nested Loop** - Using a nested loop, iterate through all pairs of words within the list.
 - **Concatenate and Check** - For every pair, concatenate them and check if the result is a palindrome using the *is_palindrome* helper function
 - **is_palindrome** - Helper function which check if the given parameter is the same compare to its reverse.
 - **Return the Results** - After checking if the concatenated pairs are palindrome, return their indices.

## Instructions to Run the Code
 - Just run the code and it will show the output for the initial sample input.
 - You can check other test cases by changing the argument for the palindrome_functions *(I made several samples to test different scenarios)*.