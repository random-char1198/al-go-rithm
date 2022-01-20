def contains_duplicates(nums):
    if len(nums) <= 1:
        return False
    else:
        nums = sorted(nums)
        n = 0
        for i in range(4):
            if nums[i] == nums[i + 1]:
                n += 1
            else:
                pass
        if n > 0:
            return True
        else:
            return False


def contains_duplicates1(nums):
    new_nums = set(nums)
    if len(nums) <= 1:
        return False
    else:

        if len(nums) > len(new_nums):
            # When the length is >, that means some items is removed from the list.
            return True
        else:
            return False


print(contains_duplicates([2, 14, 18, 22, 22]))
print(contains_duplicates1([2, 14, 18, 22, 22]))
#
