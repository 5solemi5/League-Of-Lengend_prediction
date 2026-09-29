import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import (
Dense, Conv2D, MaxPool2D, Flatten, Dropout, BatchNormalization
)
import os
import  datetime

dir_name = 'log_lol'

def make_TB_dir(dir_name):
    root_dir = os.path.join(os.curdir, dir_name)
    sub_dir_name = datetime.datetime.now().strftime("%Y%m%d-%H")
    return os.path.join(root_dir, sub_dir_name)

TB_log_dir = make_TB_dir(dir_name)
TensorB = keras.callbacks.TensorBoard(log_dir = TB_log_dir)

train_df = pd.read_csv("./match_data_platinum_train.csv")
valid_df = pd.read_csv("./match_data_platinum_val.csv")

y_train = train_df['label']
y_valid = valid_df['label']

del train_df['label']
del valid_df['label']

x_train = train_df.values
x_valid = valid_df.values

print(x_train.shape, y_train.shape)
print(x_valid.shape, y_valid.shape)

num_classes = 2

y_train = keras.utils.to_categorical(y_train, num_classes)
y_valid = keras.utils.to_categorical(y_valid, num_classes)

x_train = x_train.reshape(-1,10,5,1)
x_valid = x_valid.reshape(-1,10,5,1)

model = Sequential()
model.add(Conv2D(75, (3,3), strides=1, padding="same", activation="relu", input_shape=(10, 5, 1)))
model.add(BatchNormalization())
model.add(MaxPool2D((2,2), strides=2, padding="same"))
model.add(Conv2D(50, (3,3), strides=1, padding="same", activation="relu"))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(MaxPool2D((2,2), strides=2, padding="same"))
model.add(Conv2D(25, (3,3), strides=1, padding="same", activation="relu"))
model.add(BatchNormalization())
model.add(MaxPool2D((2,2), strides=2, padding="same"))
model.add(Flatten())
model.add(Dense(units=256, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(units=num_classes, activation="softmax"))
model.summary()

model.compile(loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=10, verbose=1, validation_data=(x_valid,y_valid),callbacks=[TensorB])

