import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    nums = np.array(list)
    nums = np.reshape(nums, (1,3,3))



    class DictVal:

        calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": [],
        }

        def __init__(self, axis):
            

    mean = DictVal()












    for i in (2, 1):
        calculations['mean'] = np.mean(nums, axis=i)
        calculations['variance'] = np.var(nums, axis=i)
        calculations['standard deviation'] = np.std(nums, axis=i)
        calculations['max'] = np.max(nums, axis=i)
        calculations['min'] = np.min(nums, axis=i)
        calculations['sum'] = np.sum(nums, axis=i)
        print(calculations)





    return calculations