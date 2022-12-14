import pandas as pd
# df = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]}, index=['a','b','c'])



data ={
    'year': [2001,2002,2003],
    'age': [10,20,30],
    'sem':  [1,2,3]
}
df = pd.DataFrame(data)
a = df.plot(x='age', y=['year','sem'], kind='bar')
print(a)

