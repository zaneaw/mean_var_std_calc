import numpy as np

nums = np.array([9, 1, 5, 3, 3, 3, 2, 9, 0])
nums = nums.reshape((1, 3, 3))

for x in (1, 2, None):
    result_list = []
    result = np.mean(nums, axis=x, dtype=None).tolist()
    result_list.append(result)

calculations = {
    "mean": result_list
}


# calculations['mean'] = [np.mean(nums, axis=1), np.mean(nums, axis=1), np.mean(nums, axis=1)]
# calculations['mean'].extend(np.mean(nums, axis=2))
# calculations['mean'].extend(np.mean(nums, axis=None))


print(calculations)