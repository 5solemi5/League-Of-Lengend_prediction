import pandas as pd
import numpy as np

df = pd.read_csv("0825_top.csv")
print(f"전체 데이터 수: {len(df)}")

# print(df["tier"])

# P E D M R C
tier_over_platinum = np.where(
    (df['tier'] == "P") |
    (df['tier'] == "E") |
    (df['tier'] == "D") |
    (df['tier'] == "M") |
    (df['tier'] == "R") |
    (df['tier'] == "C")
)

# df_fillter_tier = df.loc[tier_over_platinum]
df_fillter_tier = df
print(f"플래티넘 이상 데이터 수 : {len(df_fillter_tier)}")

df_list = [] # ~4844 덩어리
df_id_list = []

for j in range(6):
    data_frame = pd.DataFrame(
        [
            # 입력
            df_fillter_tier.iloc[j]['kda'],
            df_fillter_tier.iloc[j]['dpd'],
            df_fillter_tier.iloc[j]['dpm'],
            df_fillter_tier.iloc[j]['dpg'],
            df_fillter_tier.iloc[j]['dtpm'],
            # 출력
            df_fillter_tier.iloc[j]['tid'],
            df_fillter_tier.iloc[j]['win']
        ],
        columns=['TOP'],
        index=['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'tid', 'win']
    )
    df_list.append(data_frame)
    df_id_list.append(df_fillter_tier.iloc[j]['id'] // 10)
    print(j)

df_feature = pd.concat(df_list, keys=df_id_list)
# df_feature.to_pickle("test.pkl")
print(df_feature)