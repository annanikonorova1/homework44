import pandas as pd
import random

lst = ['cat'] * 10  # копирует 10 раз cat в массиве
lst += ['dog'] * 10  # копирует 10 раз dog в массиве и добавляет его к cat

random.shuffle(lst)  # перемешивает эл-ты в массиве
data = pd.DataFrame({'whoAmI': lst})  # создает dataframe
print(data.head())  # вывод первых 5 строк

print()

data = pd.get_dummies(data['whoAmI'], dtype=int)
print(data.head())
