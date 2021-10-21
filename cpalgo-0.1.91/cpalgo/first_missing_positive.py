def first_missing_positive(nums):
    index = 0
    while index < len(nums):
        if index + 1 == nums[index]:    
            index += 1
        elif nums[index] <= 0:       
              index += 1
        elif nums[index] > len(nums):  
               index += 1
        elif nums[index] == nums[nums[index]-1]:
            index += 1
        else:
            A,B = index,nums[index]-1
            nums[A], nums[B] = nums[B], nums[A]
            

    for index in range(len(nums)):
        if index + 1 != nums[index]:   
            return index + 1

    return len(nums) + 1