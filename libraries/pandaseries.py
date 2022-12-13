import pandas as pd

a = [1,2,3,4,5]
b = pd.Series(a)
print(b)

    # labels
print(b[4])

    # index argumet to create custom label
b = pd.Series(a, index=["a", "b", "c", "d", "e"])
print(b)
print(b["d"])


    # key/value objects as Series
routine = {
    "sunday": 'AINN',
    "monday": 'ADA',
    "tuesday": 'SP',
    "wednesday": 'AOS'
}
var = pd.Series(routine)
print(var)