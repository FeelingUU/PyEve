import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def test_pandas():
    df = DataFrame({'height': [1, 2, 3, 4], 'sex': [0, np.nan, 2, 2], 'age': [1, 1, 1, 1]})
    df.loc[0] = [0, 0, 0]
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


def test_Series():
    s = Series([1, 2, 3, 4], index=[['a', 'a', 'b', 'b'], ['第一次', '第二次', '第一次', '第二次']])
    print(s)
    print(s[['b']])
    print(s['a':'b'])
    pass


def test_DataFrame():
    # df = DataFrame(np.random.randint(0,100,size=(6,3)),
    #                columns=['语文','数学','英语'],
    #                index=[['john','john','andy','andy','jenney','jenney'],['期中','期末','期中','期末','期中','期末']])
    # df2 = DataFrame(np.random.randint(0, 100, size=(6, 3)),
    #                columns=['语文', '数学', '英语'],
    #                index=pd.MultiIndex.from_arrays([['john', 'john', 'andy', 'andy', 'jenney', 'jenney'], ['期中', '期末', '期中', '期末', '期中', '期末']]))
    # df3 = DataFrame(np.random.randint(0, 100, size=(6, 3)),
    #                 columns=['语文', '数学', '英语'],
    #                 index=pd.MultiIndex.from_tuples(
    #                     (('a','1'),('a','2'),('b','1'),('b','2'),('c','1'),('c','2'))))
    df4 = DataFrame(np.random.randint(0, 100, size=(6, 3)),
                    columns=pd.MultiIndex.from_product([['语文', '数学', '英语']]),
                    index=pd.MultiIndex.from_product(
                        [['andy', 'john', 'jenney'], ['1', '2']]))
    df4.sort_index(inplace=True)
    print(df4)
    print(df4.loc["andy":"john"])


if __name__ == '__main__':
    test_DataFrame()
