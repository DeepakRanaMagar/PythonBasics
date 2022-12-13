# library used to work with data set
# has function for analyzing, cleaning, storing and manipulating data
# pandas -> panel data and python data analysis
# abilities of pandas : 
# is there any correlation between two or more columns, what is avg value, min value, max value, delete irrelevent rows(empty or null values)



import pandas as pd
dataSet = {
    'cars': ["BMW", "LAMBO", "FERRARI"],
    'price': [1000, 2000, 3000 ]
}
var = pd.DataFrame(dataSet)
print(var)