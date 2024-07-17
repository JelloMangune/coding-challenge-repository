# Problem Set 3: Longest Increasing Subsequence

## Problem Description
Given an unsorted array of integers, find the length of the longest increasing subsequence.

## Solution Overview
 - **Initialize an array** - *incre_subseq_length* is created with all elements set to 1. This will store the length of the longest increasing subsequence (LIS) ending with each index. 
 - **Nested Loop** - iterate through each element in the input list *nums[i]*.
    - For every current element, iterate through all of its previous elements *nums[j]*.
    - If the previous element *nums[j]* is less than the current element *nums[i]*, it means that we can extend the length of the LIS of that element. Hence, we update the *incre_subseq_length[i]* to be the maximum of its current value or *incre_subseq_length[j]*.
 - **Result** - The result will be the maximum value in the *incre_subseq_length*.

## Instructions to Run the Code
 - Just run the code and it will show the output for the initial sample input.
 - You can check other test cases by changing the argument for the lengthOfLIS function *(I made various sample inputs to test different scenarios)*.