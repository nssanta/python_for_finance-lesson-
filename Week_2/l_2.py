from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

    ms = pd.read_csv('../Data/microsoft.csv', index_col=0)
    print(ms.head())

    # Вычисляем логорифмическую доходность
    ms['LogReturn'] = np.log(ms['Close']).shift(-1) - np.log(ms['Close'])

    # Вычисляем среднее , и стандартное отклонение
    mu = ms['LogReturn'].mean()
    sigma = ms['LogReturn'].std(ddof=1)
    # Создаем массив , заполняем лог.доходностью с шагом 0.001, и вычисляем PDF на основе полученных данныъ выше.
    density = pd.DataFrame()
    density['x'] = np.arange(ms['LogReturn'].min() - 0.01, ms['LogReturn'].max() + 0.01, 0.001)
    density['pdf'] = norm.pdf(density['x'], mu, sigma)
    # Строим гистограмму лог.доходность и кривую для распределения плотности(PDF)
    ms['LogReturn'].hist(bins=50, figsize=(15, 8))
    plt.plot(density['x'], density['pdf'], color='red')
    plt.show()

    # Вероятность падения дневной лог.доходности на 5 процентов
    prob_return1 = norm.cdf(-0.05, mu, sigma)
    print('The Probability is ', prob_return1)

    # Вероятность падения на 40 процентов за 220 дней
    mu220 = 220 * mu
    sigma220 = (220 ** 0.5) * sigma
    print('The probability of dropping over 40% in 220 days is ', norm.cdf(-0.4, mu220, sigma220))


    # Ищем 5 процентов порог в нормальном распределении данных, а именно статистическая мера риска. ( квантиль)
    VaR = norm.ppf(0.05, mu, sigma)
    print('Single day value at risk ', VaR)

    # Выведем 5 процентый и 95 процентный квантиль
    print('5% quantile ', norm.ppf(0.05, mu, sigma))
    print('95% quantile ', norm.ppf(0.95, mu, sigma))




if __name__ == '__main__':
    main()
