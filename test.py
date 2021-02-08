import numpy as np

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
nums = np.reshape(nums, (3, 3))

mean_list = []
var_list = []
std_list = []
max_list = []
min_list = []
sum_list = []

calculations = {
    "mean": mean_list,
    "variance": var_list,
    "standard deviation": std_list,
    "max": max_list,
    "min": min_list,
    "sum": sum_list,
}
calc = ("mean", "var", "std", "max", "min", "sum")

for x in calc:
    add_list = eval(x + "_list")
    j = eval("np." + x + "(nums, axis=1).tolist()")
    for y in (0, 1, None):
        add_list.append(j)

print(calculations)


# def dict_func(k):
#     keys_list = []
#     for y in (0, 1, None):
#         keys_list.append(np.k(nums, axis=y).tolist())
#     return keys_list

# D.R.Y.
# calculations = {
#     "mean": [np.mean(nums, axis=0).tolist(), np.mean(nums, axis=1).tolist(), np.mean(nums, axis=None).tolist()],
#     "variance": [np.var(nums, axis=0).tolist(), np.var(nums, axis=1).tolist(), np.var(nums, axis=None).tolist()]
#     "standard deviation": ,
#     "max": ,
#     "min": ,
#     "sum": ,
# }
# print(calculations)