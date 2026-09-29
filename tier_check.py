import pandas as pd
import numpy as np

df = pd.read_pickle("0917_plus_game_data.pkl")

ids = set()

for id, _, _ in df.index:
    ids.add(id)

ids = sorted(ids)

tier_dict = {"U" : 0, "I" : 1, "B" : 2, "S" : 3, "G" : 4, "P" : 5, "E" : 6, "D" : 7, "M" : 8, "R" : 9, "C" : 10}

idx = pd.IndexSlice

num_is_platinum = 0
num_avg_platinum = 0

is_platinum_id = []

for id in ids:
    tier_data = df.loc[idx[id, :, 'tier']].values
    tier_data = list(np.concatenate(tier_data))
    is_platinum = 0
    over_platinum = 0
    for tier in tier_data:
        is_platinum += int(tier_dict[tier] >= 5)
        over_platinum += int(tier_dict[tier])
    over_platinum = over_platinum / 10
    print(id, is_platinum, over_platinum)

    if is_platinum == 10:
        num_is_platinum += 1
        is_platinum_id.append(id)
    if over_platinum >= 5.0:
        num_avg_platinum += 1

df_platinum = df.loc[idx[is_platinum_id]]
df_platinum.to_pickle("0917_plus_game_data_is_platinum.pkl")
print(num_is_platinum)