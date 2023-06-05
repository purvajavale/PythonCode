import pandas as pd
import openpyxl as op


def dataClean():
    file = pd.read_excel(r"E:\PURVA\Machine Learning\ml-25m\Customer Call List.xlsx")
    df = file.drop_duplicates()
    print(df)
    df = df.drop(columns="Not_Useful_Column")
    print(df)
    df["Last_Name"] = df["Last_Name"].str.strip("123._/")
    print(df)
    df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
    df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')
    print(df)
    # df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', 2, expand=True)
    # print(df)
    df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
    df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
    print(df)
    df = df.fillna('')
    print(df)

    for x in df.index:
        if df.loc[x, "Do_Not_Contact"] == 'Y':
            df.drop(x, inplace=True)
    print(df)


if __name__ == '__main__':
    dataClean()
