import pandas as pd
# データフレームの作成
data = {'名前': ['太郎', '次郎', '花子', '三郎'],
        '年齢': [25, 30, 20, 35],
        '性別': ['男', '男', '女', '男']}
df = pd.DataFrame(data)
# データフレームの表示
print(df)
# 年齢の平均値を計算
average_age = df['年齢'].mean()
print(f'年齢の平均値: {average_age}')
# 名前が「太郎」の行を抽出
taro_row = df[df['名前'] == '太郎']
print(taro_row)
