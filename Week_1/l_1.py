import pandas as pd

import matplotlib.pyplot as plt

def main():

    ms = pd.read_csv('../Data/facebook.csv', index_col=0)
    fb = pd.read_csv('../Data/facebook.csv', index_col=0,)
    print(f'type fb = {type(fb)} , type ms = {type(ms)} \n')

    print(fb.head())

    #print (fb.index[-1])
    #print(fb.columns)
    #print(fb.shape)
    #print(fb.tail())
    #print(fb.describe())

    # print(fb.loc['2015-01-02', 'Close'])
    # print(fb.iloc[3,3])
    # print(fb.iloc[624, :])

    fb.loc['2015-01-01':'2015-12-31', 'Close'].plot()
    plt.show()



    # print(ms.columns.tolist())
    # for row in range(10):
    #     for col in range(len(ms.iloc[row])):
    #         print(ms.iloc[row, col], end=" | ")
    #     print()



if __name__ == '__main__':
    main()