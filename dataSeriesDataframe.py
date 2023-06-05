import pandas as pd
import numpy as np


def data_SeriesDataframe():
    my_list = [10, 25, 35]
    x = np.array(my_list)
    print(x)
    print(type(x))

    # Series- One-dimensional ndarray with axis labels (including time series)
    y = pd.Series(my_list)
    print(y)
    print(type(y))

    # Dataframe
    ice_cream = [['MCC', 1], ['Butterscotch', 2], ['Butter Pecan', 3]]
    ice_cream_dataframe = pd.DataFrame(ice_cream, index=['Flavor 1', 'Flavor 2', 'Flavor 3'],
                                       columns=('Flavor', 'Scoops'))
    print(ice_cream_dataframe)
    print(type(ice_cream_dataframe))


if __name__ == '__main__':
    data_SeriesDataframe()
