def solution(nums):
    answer = 0
    len_nums = len(nums)
    half_nums = int(len_nums / 2)
    
    answer = half_nums
    
    if len(set(nums)) < half_nums:
        answer = len(set(nums))
    
    return answer