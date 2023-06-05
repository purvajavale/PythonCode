import pandas as pd


def read_file():
    file = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\movies.csv")
    print(file.columns)
    print(file)

    # df = pd.read_table(r"E:\PURVA\Machine Learning\ml-25m\movies.csv", sep=',')
    # print(df)
    # df1 = pd.read_json(r"E:\PURVA\Machine Learning\ml-25m\movies.json")
    # df2 = pd.read_excel(r"E:\PURVA\Machine Learning\ml-25m\movies.xlsx", sheet_name = 'Sheet1')

    pd.set_option('display.max.rows', 62423)
    pd.set_option('display.max.columns', 3)
    print(file.info)
    # Return a tuple representing the dimensionality of the DataFrame.
    print(file.shape)
    # Return the first n rows.
    print(file.head(5))
    # Return the last n rows.
    print(file.tail(5))
    # Get column data from column name
    print(file['title'])
    # Access a group of rows and columns by label(s) or a boolean array.
    print(file.loc['Toy Story (1995)'])
    # integer-location based indexing for selection by position.
    print(file.iloc[10])


if __name__ == '__main__':
    read_file()
