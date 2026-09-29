import pandas as pd
import numpy as np

# df = pd.read_csv("0825_top.csv")
# df_mid = pd.read_csv("0825_mid.csv")
# df_jug = pd.read_csv("0825_jug.csv")
# df_spt = pd.read_csv("0825_spt.csv")
# df_adc = pd.read_csv("0825_adc.csv")

df = pd.read_csv("0917_top.csv")
df_mid = pd.read_csv("0917_mid.csv")
df_jug = pd.read_csv("0917_jug.csv")
df_spt = pd.read_csv("0917_spt.csv")
df_adc = pd.read_csv("0917_adc.csv")

print(f"TOP 데이터 수 : {len(df)}")
print(f"MID 데이터 수 : {len(df_mid)}")

df_list = []
df_id_list = []

for j in range(0,len(df),2):
    sub_df_list = []
    sub_df_id_list = []
    blue_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j]['kda'],             df_mid.iloc[j]['kda'],            df_jug.iloc[j]['kda'],            df_spt.iloc[j]['kda'],            df_adc.iloc[j]['kda']],
            [df.iloc[j]['dealt'],           df_mid.iloc[j]['dealt'],          df_jug.iloc[j]['dealt'],          df_spt.iloc[j]['dealt'],          df_adc.iloc[j]['dealt']],
            [df.iloc[j]['dpm'],             df_mid.iloc[j]['dpm'],            df_jug.iloc[j]['dpm'],            df_spt.iloc[j]['dpm'],            df_adc.iloc[j]['dpm']],
            [df.iloc[j]['dealttaken'],      df_mid.iloc[j]['dealttaken'],     df_jug.iloc[j]['dealttaken'],     df_spt.iloc[j]['dealttaken'],     df_adc.iloc[j]['dealttaken']],
            [df.iloc[j]['kill_at14'],       df_mid.iloc[j]['kill_at14'],      df_jug.iloc[j]['kill_at14'],      df_spt.iloc[j]['kill_at14'],      df_adc.iloc[j]['kill_at14']],
            [df.iloc[j]['diffdpm'],         df_mid.iloc[j]['diffdpm'],        df_jug.iloc[j]['diffdpm'],        df_spt.iloc[j]['diffdpm'],        df_adc.iloc[j]['diffdpm']],
            [df.iloc[j]['diffgold'],        df_mid.iloc[j]['diffgold'],       df_jug.iloc[j]['diffgold'],       df_spt.iloc[j]['diffgold'],       df_adc.iloc[j]['diffgold']],
            [df.iloc[j]['cs100'],           df_mid.iloc[j]['cs100'],          df_jug.iloc[j]['cs100'],          df_spt.iloc[j]['cs100'],          df_adc.iloc[j]['cs100']],
            [df.iloc[j]['goldearned100'],   df_mid.iloc[j]['goldearned100'],  df_jug.iloc[j]['goldearned100'],  df_spt.iloc[j]['goldearned100'],  df_adc.iloc[j]['goldearned100']],
            [df.iloc[j]['visionscore100'],  df_mid.iloc[j]['visionscore100'], df_jug.iloc[j]['visionscore100'], df_spt.iloc[j]['visionscore100'], df_adc.iloc[j]['visionscore100']],
            [df.iloc[j]['dragon100'],       df_mid.iloc[j]['dragon100'],      df_jug.iloc[j]['dragon100'],      df_spt.iloc[j]['dragon100'],      df_adc.iloc[j]['dragon100']],
            [df.iloc[j]['baron100'],        df_mid.iloc[j]['baron100'],       df_jug.iloc[j]['baron100'],       df_spt.iloc[j]['baron100'],       df_adc.iloc[j]['baron100']],
            [df.iloc[j]['tower100'],        df_mid.iloc[j]['tower100'],       df_jug.iloc[j]['tower100'],       df_spt.iloc[j]['tower100'],       df_adc.iloc[j]['tower100']],
            [df.iloc[j]['win'],             df_mid.iloc[j]['win'],            df_jug.iloc[j]['win'],            df_spt.iloc[j]['win'],            df_adc.iloc[j]['win']],
            [df.iloc[j]['tier'],            df_mid.iloc[j]['tier'],           df_jug.iloc[j]['tier'],           df_spt.iloc[j]['tier'],           df_adc.iloc[j]['tier']]
        ],
        columns=['TOP','MID', 'JUG', 'SPT', 'ADC'],
        index=['kda', 'dealt', 'dpm', 'dealttaken', 'kill_at14', 'diffdpm', 'diffgold', 'cs', 'goldearned', 'visionscore', 'dragon', 'baron', 'tower', 'win', 'tier']
    )
    sub_df_list.append(blue_data_frame)
    sub_df_id_list.append(df.iloc[j]['tid'])
    red_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j+1]['kda'],             df_mid.iloc[j+1]['kda'],            df_jug.iloc[j+1]['kda'],            df_spt.iloc[j+1]['kda'],            df_adc.iloc[j+1]['kda']],
            [df.iloc[j+1]['dealt'],           df_mid.iloc[j+1]['dealt'],          df_jug.iloc[j+1]['dealt'],          df_spt.iloc[j+1]['dealt'],          df_adc.iloc[j+1]['dealt']],
            [df.iloc[j+1]['dpm'],             df_mid.iloc[j+1]['dpm'],            df_jug.iloc[j+1]['dpm'],            df_spt.iloc[j+1]['dpm'],            df_adc.iloc[j+1]['dpm']],
            [df.iloc[j+1]['dealttaken'],      df_mid.iloc[j+1]['dealttaken'],     df_jug.iloc[j+1]['dealttaken'],     df_spt.iloc[j+1]['dealttaken'],     df_adc.iloc[j+1]['dealttaken']],
            [df.iloc[j+1]['kill_at14'],       df_mid.iloc[j+1]['kill_at14'],      df_jug.iloc[j+1]['kill_at14'],      df_spt.iloc[j+1]['kill_at14'],      df_adc.iloc[j+1]['kill_at14']],
            [df.iloc[j+1]['diffdpm'],         df_mid.iloc[j+1]['diffdpm'],        df_jug.iloc[j+1]['diffdpm'],        df_spt.iloc[j+1]['diffdpm'],        df_adc.iloc[j+1]['diffdpm']],
            [df.iloc[j+1]['diffgold'],        df_mid.iloc[j+1]['diffgold'],       df_jug.iloc[j+1]['diffgold'],       df_spt.iloc[j+1]['diffgold'],       df_adc.iloc[j+1]['diffgold']],
            [df.iloc[j+1]['cs200'],           df_mid.iloc[j+1]['cs200'],          df_jug.iloc[j+1]['cs200'],          df_spt.iloc[j+1]['cs200'],          df_adc.iloc[j+1]['cs200']],
            [df.iloc[j+1]['goldearned200'],   df_mid.iloc[j+1]['goldearned200'],  df_jug.iloc[j+1]['goldearned200'],  df_spt.iloc[j+1]['goldearned200'],  df_adc.iloc[j+1]['goldearned200']],
            [df.iloc[j+1]['visionscore200'],  df_mid.iloc[j+1]['visionscore200'], df_jug.iloc[j+1]['visionscore200'], df_spt.iloc[j+1]['visionscore200'], df_adc.iloc[j+1]['visionscore200']],
            [df.iloc[j+1]['dragon200'],       df_mid.iloc[j+1]['dragon200'],      df_jug.iloc[j+1]['dragon200'],      df_spt.iloc[j+1]['dragon200'],      df_adc.iloc[j+1]['dragon200']],
            [df.iloc[j+1]['baron200'],        df_mid.iloc[j+1]['baron200'],       df_jug.iloc[j+1]['baron200'],       df_spt.iloc[j+1]['baron200'],       df_adc.iloc[j+1]['baron200']],
            [df.iloc[j+1]['tower200'],        df_mid.iloc[j+1]['tower200'],       df_jug.iloc[j+1]['tower200'],       df_spt.iloc[j+1]['tower200'],       df_adc.iloc[j+1]['tower200']],
            [df.iloc[j+1]['win'],             df_mid.iloc[j+1]['win'],            df_jug.iloc[j+1]['win'],            df_spt.iloc[j+1]['win'],            df_adc.iloc[j+1]['win']],
            [df.iloc[j+1]['tier'],            df_mid.iloc[j+1]['tier'],           df_jug.iloc[j+1]['tier'],           df_spt.iloc[j+1]['tier'],           df_adc.iloc[j+1]['tier']]
        ],
        columns=['TOP','MID', 'JUG', 'SPT', 'ADC'],
        index=['kda', 'dealt', 'dpm', 'dealttaken', 'kill_at14', 'diffdpm', 'diffgold', 'cs', 'goldearned', 'visionscore', 'dragon', 'baron', 'tower', 'win', 'tier']
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
df_feature.to_pickle("0917_plus_game_data.pkl")
print(df_feature.head())