import pandas as pd
import matplotlib.pyplot as plt

def main():
    fb = pd.read_csv('../Data/facebook.csv', index_col = 0)
    print(fb.head(2),'\n')
    # Разница цены между двумя днями
    fb['PriceDiff'] = fb['Close'].shift(-1) - fb['Close']

    # Установка параметра display.width
    pd.set_option('display.max_columns', None)
    print(fb.iloc[0:2].to_string(line_width=1000),'\n')
    # Процентная разница цены.
    fb['Returns'] = fb['PriceDiff'] / fb['Close']
    print(fb.iloc[0:2].to_string(line_width=1000),'\n')

    # Средня для 40 свечей и 200
    fb['MA40'] = fb['Close'].rolling(40).mean()
    fb['MA200'] = fb['Close'].rolling(200).mean()
    print(fb.iloc[0:2].to_string(line_width=1500))

    plt.figure(figsize=(20,10))
    fb['Close'].loc['2015-01-01':'2015-12-31'].plot(label='Close')
    fb['MA40'].loc['2015-01-01':'2015-12-31'].plot(label='MA40')
    fb['MA200'].loc['2015-01-01':'2015-12-31'].plot(label='MA200')
    plt.legend()
    plt.show()






if __name__ == '__main__':
    main()