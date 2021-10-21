def two_sum (nums, target):
    complement ={}
    for i,v in enumerate(nums):
        if v in complement:
            return complement[v],i
        else:
            complement[target - v] = i
    return -1