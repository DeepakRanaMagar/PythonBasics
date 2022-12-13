import pandas as pd 

# data = {
#     "subject": ['ADA', 'AOS', 'AINN'],
#     "hours": [10, 20, 30]
# }
# var = pd.DataFrame(data, index=["sunday","monday", "tuesday"])
# print(var)

#     # locate
# print(var.loc["monday"])

    # load files into data frames
df = pd.read_csv('cvsfile.cvs')
print(df.to_string())