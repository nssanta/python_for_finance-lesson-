import pandas as pd
import matplotlib.pyplot as plt

def main():

    fb = pd.read_csv('../Data/facebook.csv', index_col=0)
    print(fb.head)
    # setting
    pd.set_option('display.max_column',None)
    # Средн.скольз
    fb['MA10'] = fb['Close'].rolling(10).mean()
    fb['MA50'] = fb['Close'].rolling(50).mean()
    # Buy , Sell
    fb['Shares'] = [1 if fb.loc[em, 'MA10'] > fb.loc[em, 'MA50'] else 0
                    for em in fb.index]
    print(fb.iloc[0:2].to_string(line_width=1000))
    # дневная прибыли
    fb['Close1'] = fb['Close'].shift(-1)
    fb['Profit'] = [fb.loc[em, 'Close1']-fb.loc[em,'Close']
                    if fb.loc[em, 'Shares']==1 else 0
                    for em in fb.index]
    print(fb.iloc[100:105].to_string(line_width=1000))


    # кумулятивная сумма
    fb['wealth'] = fb['Profit'].cumsum()
    print(fb.tail())
    #
    fb['wealth'].plot()
    plt.show()






if __name__ == '__main__':
    main()