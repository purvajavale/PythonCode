import pandas as pd


def Join():
    file = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\Flavors.csv")
    file1 = pd.read_csv(r"E:\PURVA\Machine Learning\ml-25m\Flavors.csv")
    file.merge(file1, how = 'inner', on = ['FellowshipID', 'FirstName'])
    
    file.merge(file1, how = 'inner')
    file.merge(file1, how = 'outer')
    file.merge(file1, how = 'left')
    file.merge(file1, how = 'right')
    file.merge(file1, how = 'cross')

    file.append(file2)
    pd.concat([file,file1], join = 'outer', axis = 1)


if __name__ == '__main__':
    Join()
