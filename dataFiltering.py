import pandas as pd


def filter_file():
    file = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\movies.csv")
    print(file.columns)
    print(file[file['movieId'] <= 5])

    specific_movies = ['Jumanji (1995)', 'Heat (1995)']
    # Return a boolean Series showing whether each element in the Series matches an element
    # in the past sequence of values exactly.
    print(file[file['title'].isin(specific_movies)])
    # Return a boolean Series showing whether each element in the Series matches an element
    # in the past sequence of values.
    print(file[file['title'].str.contains('Jumanji')])
    # print(file.filter(like='Jumanji', axis=0))
    print(file[file['movieId'] < 5].sort_values(by=['movieId', 'title'], ascending=[False, True]))


if __name__ == '__main__':
    filter_file()
