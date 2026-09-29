import numpy as np
import tensorflow as tf
import pandas as pd

path = "D:/MyRollproject/MID.csv"
df = pd.read_csv(path, encoding="ANSI")

selected_columns = df[['xpm', 'gpm', 'dpm', 'dpd']]  # 컬럼 이름 사용
X = selected_columns.values
y = df['win'].values     # 라벨 컬럼

# 모델 생성
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, input_dim=4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 모델 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(X, y, epochs=20, verbose=1)

# 학습된 모델 저장
model.save('my_model.h5')