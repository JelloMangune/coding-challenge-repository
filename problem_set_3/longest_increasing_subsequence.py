def lengthOfLIS(nums):
    if not nums:
        return 0
    
    n = len(nums)
    incre_subseq_length = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                incre_subseq_length[i] = max(incre_subseq_length[i], incre_subseq_length[j] + 1)
    
    return max(incre_subseq_length)

input_numbers = [10, 9, 2, 5, 3, 7, 101, 18]
input_numbers2 = [3, 10, 2, 1, 20]
input_numbers3 = [10, 9, 2, 5, 3, 7, 101, 18]
input_numbers4 = [10]

result = lengthOfLIS(input_numbers)
print(result) 