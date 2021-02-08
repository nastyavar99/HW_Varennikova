import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('administration_data.csv')

plt.figure(figsize=(15, 5))

male = df['gender'] == 'Male'
female = df['gender'] == 'Female'

plt.plot(df[male].groupby('age').agg({'comprehension': 'mean'}), label='воспринимаемые мальчиками слова')
plt.plot(df[male].groupby('age').agg({'production': 'mean'}), label='порождаемые мальчиками слова')

plt.plot(df[female].groupby('age').agg({'comprehension': 'mean'}), label='воспринимаемые девочками слова')
plt.plot(df[female].groupby('age').agg({'production': 'mean'}), label='порождаемые девочками слова')

plt.title('Динамика усвоения русского языка', fontsize=18)
plt.xlabel('Возраст детей в месяцах', fontsize=12)
plt.ylabel('Количество воспринимаемых/порождаемых слов', fontsize=10)
plt.legend()

plt.grid(True)
plt.xticks(np.arange(8, 39, 6))
plt.yticks(np.arange(0, 701, 100))

plt.show()

# «слияния» восприятия и порождения слов наступает в 19 месяцев
