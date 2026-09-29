import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have already loaded your DataFrame df
df = pd.read_pickle('0917_plus_game_data_is_platinum.pkl')

# Define the tier dictionary
tier_dict = {"U": 0, "I": 1, "B": 2, "S": 3, "G": 4, "P": 5, "E": 6, "D": 7, "M": 8, "R": 9, "C": 10}

idx = pd.IndexSlice

# Extract tier data
tier_data = df.loc[idx[:, :, 'tier']].values

# Flatten the tier data
tier_data_1d = np.concatenate(tier_data)
tier_data_1d = list(tier_data_1d)

# Create a DataFrame
df_tier = pd.DataFrame(tier_data_1d, columns=['Tier'])

# Plot the histogram
plt.figure(figsize=(10, 6))
df_tier['Tier'].map(tier_dict).plot(kind='hist', bins=np.arange(12)-0.5, rwidth=0.8, color='skyblue', edgecolor='black')

# Customize the plot
plt.title('Distribution of Tiers')
plt.xlabel('Tier')
plt.ylabel('Count')
# plt.xticks(range(len(tier_dict)), tier_dict.keys())
#
# # Show the plot
# plt.show()

# Set bins and plot histogram
bins = np.arange(12) - 0.5
hist, edges, _ = plt.hist(df_tier['Tier'].map(tier_dict), bins=bins, rwidth=0.8, color='skyblue', edgecolor='black')


# Add count labels on top of each bar
for i in range(len(hist)):
    count = int(hist[i])
    if count > 0:
        plt.text(edges[i] + 0.4, count + 0.1, f'{count:,}', ha='center', va='bottom')

# Show the plot
plt.xticks(range(len(tier_dict)), tier_dict.keys())
plt.show()