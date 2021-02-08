import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    nums = np.reshape(list, (3, 3))

    calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": [],
    }

    for i in (0, 1, None):
        calculations["mean"] = np.mean(nums, axis=i)
        calculations["variance"] = np.var(nums, axis=i)
        calculations["standard deviation"] = np.std(nums, axis=i)
        calculations["max"] = np.max(nums, axis=i)
        calculations["min"] = np.min(nums, axis=i)
        calculations["sum"] = np.sum(nums, axis=i)
        print(calculations)

    return calculations