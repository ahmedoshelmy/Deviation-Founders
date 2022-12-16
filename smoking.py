import numpy as np
import pandas as pd


def main():
    cardio_data = pd.read_csv('cardio_train.csv', sep=';')
    smokers = cardio_data[cardio_data['smoke'] == 1]
    average_age = smokers['age'].mean()
    mode_age = smokers['age'].mode()[0]
    print('The average age of smokers ', average_age / 365)
    print('The most repeated age of smokers ', mode_age / 365)


if __name__ == "__main__":
    main()

# %%
