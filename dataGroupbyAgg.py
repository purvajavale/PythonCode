import pandas as pd


def groupBy():
    df = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\Flavors.csv")
    group_by_frame = df.groupby('Base Flavor')
    group_by_count = df.groupby('Base Flavor').count()
    group_by_sum = df.groupby('Base Flavor').sum()
    print(f'Group : {group_by_frame.describe()}')
    print(f'Group Count : {group_by_count}')
    print(f'Group sum : {group_by_sum}')


def agg():
    df = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\Flavors.csv")
    group_agg = df.groupby('Base Flavor').agg(
        {'Flavor Rating': ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum']})
    print(f'GroupAgg : {group_agg.describe()}')
    group_agg_multicolumn = df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating': ['mean', 'max', 'count', 'sum']})
    print(f'GroupAggMultipleColumn : {group_agg_multicolumn.describe()}')


if __name__ == '__main__':
    groupBy()
    agg()
