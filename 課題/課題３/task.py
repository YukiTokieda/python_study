import pandas as pd
import numpy as np
from typing import List
import datetime as dt
from sklearn import linear_model

dummy_data = pd.DataFrame({'Group': ['A'] * 50 + ['B'] * 50,
                           'Region': ['X'] * 50 + ['Y'] * 50,
                           'Date': pd.date_range('2021-01-01',periods=100, freq='w'),
                           'Var 1': 1000 * np.random.rand(100),
                           'Var 2': 1000 * np.random.rand(100)})

# 課題3-1 以下のようなpandas DataFrame “dummy_data”が入力 0として与えられた時、
# ● 入力 1 ”Group”, または“Region”もしくはその両方
# ● 入力 2 週、月、年
# を元に”Var 1”, “Var 2”の合計値を計算するPythonの関数“group_func”を書いてください。（例外の処理も含む）

# 前処理
data = pd.get_dummies( dummy_data)
data = data.drop(['Group_B','Region_Y'], axis=1)
data['sum_var'] = data['Var 1'] + data['Var 2']
data['Date'] = pd.to_datetime(data['Date'])
data['Date']=data['Date'].map(dt.datetime.toordinal)

# 重回帰分析モデル
reg1 = linear_model.LinearRegression()
reg2 = linear_model.LinearRegression()
reg3 = linear_model.LinearRegression()

# 説明変数
X1 = data[['Group_A','Date']]
X2 = data[['Region_X','Date']]
X3 = data[['Group_A','Region_X','Date']]

# 目的変数を定義する
Y = data[['sum_var']]

#  モデル作成
reg1.fit(X1,Y)
reg2.fit(X2,Y)
reg3.fit(X3,Y)

df = dummy_data
# group = ['Group'] # other possible options: ['Group', 'Region'], ['Region']
# date_aggregation = 'Week' # other possible options: "Month", "Year"

def group_func(df, group, date_aggregation):
# 入力２：日付
  if len(date_aggregation) == 10 :
    date = dt.datetime.strptime(date_aggregation, '%Y-%m-%d')
  elif len(date_aggregation) == 7:
    date = dt.datetime.strptime(date_aggregation, '%Y-%m')
  elif len(date_aggregation) == 4:
    date = dt.datetime.strptime(date_aggregation, '%Y')
  else:
    return print('エラー：日付の入力が間違っています')
  date = dt.datetime.toordinal(date)

# 入力１： ”Group”, または“Region”もしくはその両方
  group_list = ['A','B','X','Y']

  if len(group)==0:
      return print('Group または Regionの入力がありません')
  elif not set(group).issubset(group_list) or len(group)==3:
      return print('Group または Regionの入力が間違っています')
  else:
    if 'A' in group and 'B' in group:
      return print('GroupはA,Bどちらかで入力して下さい')
    elif 'A' in group:
      Group = 1
    elif 'B' in group:
      Group = 0
    else:
      Group = None

    if 'X' in group and 'Y' in group:
      return print('RegionのX,Yどちらかで入力して下さい')
    if 'X' in group:
      Region = 1
    elif 'Y' in group:
      Region = 0
    else:
      Region = None

# モデルの適応
  if Group is not None and Region  is not None:
    print('モデル3')
    result =  reg３.predict([[Group,Region,date]])
  elif Group is not None:
    print('モデル1')
    result =  reg1.predict([[Group,date]])
  elif Region  is not None :
    print('モデル2')
    result =  reg2.predict([[Region,date]])
  else:
    print('エラー')

  result = result[0][0]
  result = '予測したVar 1, Var 2の合計値は:' + str(result)

  return print(result)