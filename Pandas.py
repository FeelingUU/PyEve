import pandas as pd
from pandas import Series,DataFrame
import numpy as np

def test_pandas():
    df = DataFrame({'height':[1,2,3,4],'sex':[0,np.nan,2,2],'age':[1,1,1,1]})
    df.loc[0] = [0,0,0]
    print(df)
    print(df[df.isnull().any(axis=1)])


    # print(df.mean(0))
    # print(df.fillna(0))
    #
    # s = Series([2,3,4,56,123,23,2,1,5,23])
    #
    # print(s.value_counts())
    # ss = Series(['ESs','SDSD'])
    # print(ss.str.upper())

    # dates = pd.date_range('20130101', periods=6)
    # s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
    # print(s.shift(2))


if __name__ == '__main__':
    test_pandas()