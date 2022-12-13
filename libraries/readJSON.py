import pandas as pd
dataframe = pd.read_json('index.json')
print(dataframe.to_string())