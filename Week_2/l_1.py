import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Эмитация бросания двух кубиков

    # При одном броске
    die = pd.DataFrame([1, 2, 3, 4, 5, 6])
    sum_of_die = die.sample(2, replace=True).sum().loc[0]
    print(f'(Сумма двух бросков) sum_of_die = {sum_of_die}')

    # При 50 бросках
    iter_c = 100
    sum_of_die_100 =[die.sample(2,replace=True).sum().loc[0] for x in range(iter_c)]
    print(sum_of_die_100)

    freq = pd.DataFrame(sum_of_die_100)[0].value_counts()
    sort_f = freq.sort_index()
    # Относительная частота
    relative_f = sort_f/sort_f.sum()
    relative_f.plot(kind='bar', color='orange')
    plt.show()

    print(sort_f)



if __name__ == '__main__':
    main()