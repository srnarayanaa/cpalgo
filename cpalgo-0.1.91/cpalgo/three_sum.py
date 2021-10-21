def three_sum(nums, target):
    nums.sort()
    length = len(nums)
    result = set()
    for i in range(length-2):
        left = i+1
        right = length-1
        while left < right:
            sum_value = nums[i]+nums[left]+nums[right]
            if sum_value == 0:
                result.add((nums[i],nums[left],nums[right]))
                left += 1
                right -= 1
            elif sum_value < 0:
                left +=1
            else:
                right -= 1
    return result