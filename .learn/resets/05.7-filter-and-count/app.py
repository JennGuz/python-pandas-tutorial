import pandas as pd

# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# print(data_frame)

# [23,45,7,34,6,63,36,78,54,34]

# data = pd.Series([23,45,7,34,6,63,36,78,54,34])

# print(data)

# data = pd.date_range(start='2021-05-01', end='2021-05-12')

# print(data)

# my_series = pd.Series([2, 4, 6, 8, 10])

# my_series = my_series.apply(lambda x: x/2)

# print(my_series)

# data = [
#     { 
#         "brand": "Toyota", 
#         "model": "Corolla",
#         "color": "Blue"
#     },
#     {
#         "brand": "Ford", 
#         "model": "K",
#         "color": "Yellow"
#     },
#     {
#         "brand": "Porsche", 
#         "model": "Cayenne",
#         "color": "White"
#     }
# ]

# df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
# df = pd.DataFrame(data)
# df.loc[len(df)] = ['Tesla', 'Model S', 'Red']

df = pd.read_csv('.learn/assets/pokemon_data.csv')
print(df.loc[df['legendary'].len])


# selected_columns = df[['Name', 'Type 1']]
# print(selected_columns.head(10))
# print(df.iloc[133,6])