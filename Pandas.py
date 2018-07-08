import pandas as pd
from pandas import Series, DataFrame
import numpy as np


def test_pandas():
    df = DataFrame({'height': [1, 2, 3, 4], 'sex': [0, 2, 0, 2], 'age': [1, 1, 1, 0]})
    df.loc[0] = [0, 0, 0]
    print(df)
    print(df.groupby(['age', 'sex']).sum())

    # print(df[df.isnull().any(axis=1)])
    # print(df.mean(1))
    # print(df.sum(1))
    # print(df.std(1))
    # print(df.min(1))

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
    # df4 = DataFrame(np.random.randint(0, 100, size=(6, 3)),
    #                 columns=pd.MultiIndex.from_product([['语文', '数学', '英语']]),
    #                 index=pd.MultiIndex.from_product(
    #                     [['andy', 'john', 'jenney'], ['1', '2']]))
    # df4.sort_index(inplace=True)
    #
    # df5 = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
    #                    'B': ['a', 'b', 'c'] * 4,
    #                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
    #                    'D': np.random.randn(12),
    #                    'E': np.random.randn(12)})
    # print(df5)
    # print('-----------------')
    # print(pd.pivot_table(df5, values='D', index=['A', 'B'], columns=['C']))
    # print(pd.pivot_table(df5, values='D', index=['A', 'B']))

    # index = pd.date_range('2018-01-01 23:20:01',periods=5,freq='S')
    # df6 = DataFrame(np.random.randint(0,20,size=(5,5)),index=index)

    df7 = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['e', 'e', 'b', 'a', 'a', 'e'],'name':[1,2,3,4,5,6]},
                       index=['a', 'b', 'c', 'd', 'e', 'f'],
                       columns=["id", "raw_grade","name"])
    df8 = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grades": ['aA', 'bD', 'bD', 'aD', 'aD', 'eD'],'name':[1,2,3,4,5,6]},
                       index=['C', 'D', 'e', 'f', 'g', 'h'],
                       columns=["id", "raw_grades","name"])
    # df7.index = ['A','B','C','D','E','F']
    # df7['raw_grades'] = df8.id
    # df7.loc['G'] = [7,'qq',np.nan]

    print(df7)
    print(df8)
    # print(pd.concat([df7,df8],axis=1,join_axes=[df7.index]))
    # print(pd.concat([df7,df8],axis=1,join_axes=[df8.index]))
    print(pd.merge(df7,df8,on='id'))



def test_csv():
    data = pd.read_csv('E:/2016.csv', encoding='utf-8')
    print(data)
    pass


def test_plt():
    import matplotlib.pyplot as plt
    df8 = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6], "raw_grades": [33, 22, 1, 32, 22, 111], 'name': [1, 2, 3, 4, 5, 6]},
        index=[2,3,4,5,6,7],
        columns=["id", "raw_grades", "name"])
    df8.plot()
    plt.show()
    pass

if __name__ == '__main__':
    test_plt()


