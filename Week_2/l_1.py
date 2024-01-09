import pandas as pd
import numpy as np

def main():
    # Эмитация бросания двух кубиков

    # При одном броске
    die = pd.DataFrame([1, 2, 3, 4, 5, 6])
    sum_of_die = die.sample(2, replace=True).sum().loc[0]
    print(f'(Сумма двух бросков) sum_of_die = {sum_of_die}')

    # При 50 бросках
    iter_c = 50
    sum_of_die_50 =[die.sample(2,replace=True).sum().loc[0] for x in range(iter_c)]
    print(sum_of_die_50[:])g



if __name__ == '__main__':
    main()