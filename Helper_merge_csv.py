import pandas as pd
df1 = pd.read_csv('Merged3.csv')
# df2 = pd.read_csv('FlairGenders.csv')
df2 = pd.read_csv('numCommentsByAuthor.csv')
# df2 = pd.read_csv('authors_first_last.csv')

df_merged = pd.merge(df1, df2, on="author", how="left")  # how = 'inner', left
# df_merged.to_csv('Test_merged_csv.csv')
df_merged.to_csv('Merged4.csv')
