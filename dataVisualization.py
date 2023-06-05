import pandas as pd
import matplotlib.pyplot as plt


# An object-oriented plotting library


def index_file():
    file = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\Ice Cream Ratings.csv")
    # print(file)
    file.set_index('Date')
    print(plt.style.available)
    plt.style.use('classic')
    file.plot(kind='line', title='Icecream Ratings', xlabel='Daily Ratings', ylabel='Scores')
    plt.show()
    file.plot.barh(stacked=True, title='Icecream Ratings', xlabel='Daily Ratings', ylabel='Scores')
    plt.show()
    file.plot.scatter(title='Icecream Ratings', x='Texture Rating', y='Overall Rating', s=500, c='Yellow')
    plt.show()
    file.plot.hist(title='Icecream Ratings', bins=10)
    plt.show()
    file.boxplot()
    plt.show()
    file.plot.area(title='Icecream Ratings', figsize=(10, 5))
    plt.show()
    file.plot.pie(title='Icecream Ratings', y='Flavor Rating', figsize=(10, 10))
    plt.show()


if __name__ == '__main__':
    index_file()
