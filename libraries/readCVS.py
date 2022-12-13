import pandas as pd
dataframe = pd.read_csv('cvsfile.csv')

print(dataframe.to_string())

print(dataframe)

    # max-columns
print(pd.options.display.max_columns)

    # max-rows
print(pd.options.display.max_rows)

