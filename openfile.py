import pickle

with open('0825_game_data_norm.pkl', 'rb') as f:
    data = pickle.load(f)

    print(data)

# =========================================================================
# =========================================================================

# 0825_adc.csv
# 0825_game_data.pkl

# 0825_game_data_is_platinum.pkl
# 0825_game_data_platinum_norm.pkl

# 0825_game_data_is_platinum.pkl
# match_data_over_platinum.pkl
# match_data_platinum_train.csv
# match_data_platinum_val.csv
# test.pkl
# top_data_only.pkl

# ========================================================================
# =========================================================================
# 0825_game_data.pkl
# = 0825_game_data_is_platinum.pkl 생성하는 파일

# D:\LoL_EDA\venv\Scripts\python.exe D:\LoL_EDA\openfile.py
#                              TOP      MID       JUG      SPT      ADC
# id         team feature
# 6667524844 100  kda      1.85714      3.0       4.6     2.75      1.5
#                 dpd       3932.0   5131.0    3796.8  2350.88   2417.3
#                 dpm      786.775  733.349   542.658  537.599  690.986
#                 dpg      1.85672  1.85987    1.4232  1.69662  1.66837
#                 dtpm     1191.57  688.471   1455.58  792.692  725.317
# ...                          ...      ...       ...      ...      ...
# 6669000775 200  dpm      607.414  429.801    117.99  433.068    456.0
#                 dpg      1.64422  1.52872  0.392641  1.30673   1.4873
#                 dtpm     508.272  500.921   687.895  403.853  386.702
#                 win            1        1         1        1        1
#                 tier           G        G         G        P        G
#
# [2821630 rows x 5 columns]
#
# Process finished with exit code 0
# =========================================================================
# =========================================================================
# 기본 데이터
# =========================================================================
# >lol_data_extract_to_pickle.py
# ||0825_adc.csv,0825_jug.csv,0825_mid.csv,0825_spt.csv,0825_top.csv
# >> 0825_game_data.pkl

# >navie_eda.py
# ||0825_top.csv
# >> test.pkl


# ========================================================================
# >>>> top_data_only.pkl
# ========================================================================
# >navie_eda_test_v2.py
# ||0825_top.csv, 0825_mid.csv
# >> top_data_only.pkl
#
# >data_test.py
# ||top_data_only.pkl
# >>
#
# >tier_check2.py
# ||top_data_only.pkl
# >> 0825_game_data_is_platinum.pkl

# ===========================================================================
# 0825_game_data_is_platinum.pkl
# = 0825_game_data_is_platinum_norm.pkl 생성하는 파일 by data_norm.py

# D:\LoL_EDA\venv\Scripts\python.exe D:\LoL_EDA\openfile.py
#                              TOP      MID      JUG      SPT      ADC
# id         team feature
# 6667524895 100  kda          1.4      1.5      2.5     10.0      9.5
#                 dpd       1862.4  1802.67  3430.25   4052.5  12114.5
#                 dpm      360.465  418.684  531.135  313.742  937.897
#                 dpg      1.13561  1.51379  1.44736  1.19279  1.61204
#                 dtpm     751.664  605.574  1081.16  510.735  565.548
# ...                          ...      ...      ...      ...      ...
# 6669000761 200  dpm      743.729  651.093  482.922  628.931  345.713
#                 dpg      2.30143  1.60665  1.36441  2.28239  1.06544
#                 dtpm     1005.61   745.19  1175.67  589.632  628.539
#                 win            0        0        0        0        0
#                 tier           E        P        E        P        P
#
# [629468 rows x 5 columns]
#
# Process finished with exit code 0
# ================================================================================
# ================================================================================
# >>>> 0825_game_data_is_platinum.pkl
# ================================================================================
# >data_norm.py
# ||0825_game_data_is_platinum.pkl
# >> 0825_ game_data_platinum_norm.pkl

# =========================================================================
# =========================================================================
# 0825_game_data_platinum_norm.pkl
# = forest_win.py로 승패예측

# D:\LoL_EDA\venv\Scripts\python.exe D:\LoL_EDA\openfile.py
#                               TOP       MID       JUG       SPT       ADC
# id         team feature
# 6667524895 100  kda       0.07027  0.081081  0.189189       1.0  0.945946
#                 dpd      0.114825  0.109668  0.250194   0.30392       1.0
#                 dpm      0.252993  0.328309  0.473784  0.192549       1.0
#                 dpg      0.383152  0.737202   0.67501  0.436684  0.829182
#                 dtpm     0.569056  0.377987       1.0  0.253949  0.325638
# ...                           ...       ...       ...       ...       ...
# 6669000761 200  dpm      0.438458  0.342183  0.167407  0.319151   0.02481
#                 dpg      0.908295   0.39772  0.219705  0.894303       0.0
#                 dtpm      0.54701  0.305999  0.704395  0.162034  0.198042
#                 win             0         0         0         0         0
#                 tier            E         P         E         P         P
#
# [629468 rows x 5 columns]
#
# Process finished with exit code 0
# =========================================================================
# =========================================================================
# >>>> 0825_ game_data_platinum_norm.pkl
# =========================================================================
# >data_histogram.py
# ||0825_ game_data_platinum_norm.pkl
# >>

# >data_vis.py
# ||0825_ game_data_platinum_norm.pkl
# >>

# >forest_win.py
# ||0825_game_data_platinum_norm.pkl
# >>

# >make_input.py
# ||0825_ game_data_platinum_norm.pkl
# >> match_data_over_platinum.pkl

# -----------------------------------------
# >>>> match_data_over_platinum.pkl
# -----------------------------------------
# >make_csv_data.py
# ||match_data_over_platinum.pkl
# >>

# ----------------------------------------------------------
# 제공된 데이터
# ----------------------------------------------------------
# >match_cnn.py
# ||match_data_platinum_train.csv,match_data_platinum_val.csv
# >>

