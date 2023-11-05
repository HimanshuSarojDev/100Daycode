def pair_sum(nums, target_sum):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                pairs.append((i, j))
    return pairs

my_list = [3, 2, 5, 6, 3]
my_tar = 9
result = pair_sum(my_list, my_tar)
print(result)
