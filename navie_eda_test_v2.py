import pandas as pd
import numpy as np

df = pd.read_csv("0825_top.csv")
df_mid = pd.read_csv("0825_mid.csv")

print(f"TOP 데이터 수 : {len(df)}")
print(f"MID 데이터 수 : {len(df_mid)}")

df_list = []
df_id_list = []

# 최종은 6를 len(df_filterd_tier)으로 바꿔서..
for j in range(0,6,2):
    sub_df_list = []
    sub_df_id_list = []
    blue_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j]['kda'], df_mid.iloc[j]['kda']],
            [df.iloc[j]['dpd'], df_mid.iloc[j]['dpd']],
            [df.iloc[j]['dpm'], df_mid.iloc[j]['dpm']],
            [df.iloc[j]['dpg'], df_mid.iloc[j]['dpg']],
            [df.iloc[j]['dtpm'], df_mid.iloc[j]['dtpm']],
            [df.iloc[j]['win'], df_mid.iloc[j]['win']]
        ],
        columns=['TOP','MID'],
        index=['kda', 'dpd', 'dpm', 'dpg', 'dtpm','win']
    )
    sub_df_list.append(blue_data_frame)
    sub_df_id_list.append(df.iloc[j]['tid'])
    red_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j+1]['kda'], df_mid.iloc[j+1]['kda']],
            [df.iloc[j+1]['dpd'], df_mid.iloc[j+1]['dpd']],
            [df.iloc[j+1]['dpm'], df_mid.iloc[j+1]['dpm']],
            [df.iloc[j+1]['dpg'], df_mid.iloc[j+1]['dpg']],
            [df.iloc[j+1]['dtpm'], df_mid.iloc[j+1]['dtpm']],
            [df.iloc[j+1]['win'], df_mid.iloc[j+1]['win']]
        ],
        columns=['TOP', 'MID'],
        index=['kda', 'dpd', 'dpm', 'dpg', 'dtpm', 'win']
    )
    sub_df_list.append(red_data_frame)
    sub_df_id_list.append(df.iloc[j+1]['tid'])
    sub_df_feature = pd.concat(sub_df_list, keys=sub_df_id_list, names=['team', 'feature'])
    df_list.append(sub_df_feature)
    df_id_list.append(df.iloc[j]['id'] // 10)
    blue_id = df.iloc[j]['id'] // 10
    red_id = df.iloc[j+1]['id'] // 10
    if(blue_id != red_id):
        print("아이디가 안맞아요")
    print(j)

df_feature = pd.concat(df_list, keys=df_id_list,names=['id'])
#df_feature.to_pickle("top_data_only.pkl")
print(df_feature)
