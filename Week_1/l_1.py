import pandas as pd


def main():

    ms = pd.read_csv('../Data/facebook.csv', index_col=0)
    fb = pd.read_csv('../Data/facebook.csv', index_col=1)
    print(f'type fb = {type(fb)} , type ms = {type(ms)}')

    rows =''
    print(ms.columns.tolist())
    for row in range(10):
        for col in range(len(ms.iloc[row])):
            print(ms.iloc[row, col], end=" | ")
        print()



if __name__ == '__main__':
    main()