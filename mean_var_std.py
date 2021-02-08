import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    nums = np.reshape(list, (3, 3))

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
        j = eval("np." + x)
        for y in (0, 1, None):
            add_list.append(j(nums, axis=y).tolist())

    return calculations

print(calculate([9,1,5,3,3,3,2,9,0]))
print(calculate([2,6,2,8,4,0,1,5,7]))