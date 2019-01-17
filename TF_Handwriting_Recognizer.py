import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf


from Drawer2 import Draw



mnist = tf.keras.datasets.mnist


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


"""Uncomment the following to get a feel for the data"""
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])


model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])


model.fit(x_train, y_train, epochs=5)

draw_exit = False
while draw_exit == False:
    new_label = model.predict([[Draw()]])


    prediction = np.argmax(new_label)


    print(prediction)
    print("Do you wish to exit? (Y for yes, all other for no)")
    if input() == "Y":
        draw_exit = True


