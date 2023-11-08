from read_data_img import *
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

#Charger les donnees d'entrainement et de test 

#(train_images, train_labels), (test_images, test_labels) = datasets.cifar100.load_data()
'''
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
    
file="/home/meka/Documents/INFO L2 2022-2023/Semestre 2/Data Science/Data Sciences TP/CNN-avec-librerie/cifar-10-python/cifar-10-batches-py/data_batch_1"
data=unpickle(file)
train_images=data[b'data'].reshape(10000,3,32,32).transpose(0,2,3,1)
train_labels=np.array(data[b'batch_label'])


file="/home/meka/Documents/INFO L2 2022-2023/Semestre 2/Data Science/Data Sciences TP/CNN-avec-librerie/cifar-10-python/cifar-10-batches-py/test_batch"
data=unpickle(file)
test_images=data[b'data'].reshape(10000,3,32,32).transpose(0,2,3,1)
test_labels=np.array(data[b'batch_label'])

test_images=test_images
test_labels=test_labels
'''
#Normalisation des donnees

train_images, test_images = train_images / 255.0, test_images / 255.0

#Creation du modele de reseau de neurones convolutif

model = models.Sequential()

model.add(layers.Input(32,32,3))

model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(16, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

model.add(layers.Conv2D(8, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.2))

#Ajout des couches de classification

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(100, activation='softmax'))

#Compilation du modele

model.compile(optimizer='adam',

loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

#Entrainement du modele

history = model.fit(train_images, train_labels, epochs=10000, validation_data=(test_images, test_labels))

loss_curve=history.history["loss"]
acc_curve=history.history["accuracy"]

loss_val_curve=history.history["val_loss"]
acc_val_curve=history.history["val_accuracy"]

plt.figure()
plt.plot(loss_curve, label="Train_loss")
plt.plot(loss_val_curve, label="Val_loss")
plt.legend(loc="upper left")
plt.title("loss")
plt.savefig("loss_fig.png")
plt.close()

plt.figure()
plt.plot(acc_curve, label="Train_acc")
plt.plot(acc_val_curve, label="Val_acc")
plt.legend(loc="upper left")
plt.title("accuracy")
plt.savefig("acc_fig.png")
plt.close()
#Evaluation du modele

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)

#Affichage des resultats

model.summary()


print('\nTest accuracy:', test_acc,"\nTest Loss:", test_loss)

#Sauvegarde du modèle

model.save('cnn_avec_bibiotheque.h5')
