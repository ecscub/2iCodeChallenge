# Write a function which takes 2 parameters: an array of whole numbers and an
# integer X.

# The function should look for pairs of numbers in the array which sum to X.
# Each array element can only be used in one pair. The function should return
# the count of how many such pairs it finds.

# You may assume that the array passed to the function has already been sorted
# in ascending order.

# State any assumptions or design choices you have made.


# nums = [1, 2, 3, 4, 5]
# X = 6
# result = count_pairs_with_sum(nums, X)
# print(result)

def count_pairs_with_sum(array_nums, X):
    hash_map = {}
    count = 0

    for num in array_nums:
        val = X - num
        if val in hash_map and hash_map[val] > 0:
            count += 1
            hash_map[val] -= 1
        else:
            hash_map[num] = hash_map.get(num, 0) + 1

    return count
