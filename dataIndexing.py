import pandas as pd


# stores axis labels for the panda objects
# pass is a null operation — when it is executed, nothing happens.
# It is useful as a placeholder when a statement is required syntactically,
# but no code needs to be executed
def index_file():
    file = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\movies.csv", index_col="movieId")
    print(file)
    # Reset the index of the DataFrame, and use the default one instead
    file.reset_index(inplace=True)
    # Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length).
    file.set_index('movieId', inplace=True)
    file.sort_index()


if __name__ == '__main__':
    index_file()
