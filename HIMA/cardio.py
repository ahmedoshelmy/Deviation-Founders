import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cardio_data = pd.read_csv('../cardio_train.csv', sep=';')
hascardio = cardio_data[cardio_data['cardio'] == 1]
hascardio['age'] = hascardio['age'] / 365
mean_age = hascardio['age'].mean()
mode_age = hascardio['age'].mode()[0]
median_age = hascardio['age'].median()
max_age = hascardio['age'].max()
min_age = hascardio['age'].min()
std_age = hascardio['age'].std()

print('The average age that has cardio ', median_age)
print('The median age that has cardio ', mean_age)
print('The most frequent age that has cardio ', mode_age )
print('The older age that has cardio ', max_age )
print('The smaller age that has cardio ', min_age )
print('The Standard Deviation of the ages that have cardio ', std_age )

print(hascardio)
plt.ylabel('Ages')
plt.title("Has cardio age box plot")
plt.boxplot(hascardio['age'])
plt.show()