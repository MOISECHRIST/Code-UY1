from read_data_img import *
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


#Utilisation du modèle sauvegardé

loaded_model=tf.keras.models.load_model('cnn_avec_bibiotheque.h5')
from PIL import Image
import numpy as np

img_path = input("Entrez le chemin de l' image : ")
img = Image.open(img_path)
img = img.resize((32, 32))
img_arr = np.array(img)
print(img_arr.shape)
img_arr = img_arr.reshape(1, 32, 32, 3)
predictions = loaded_model.predict(img_arr)
class_names =['castor', 'dauphin', 'loutre', 'phoque', 'baleine',"poissons d'aquarium", "poissons plats", "raie", "requin", "truite","orchidées", "coquelicots", "roses", "tournesols", "tulipes","bouteilles", "bols", "canettes", "gobelets", "assiettes"]
class_names +=["pommes", "champignons", "oranges", "poires", "poivrons","Horloge", "clavier d'ordinateur", "lampe", "téléphone", "télévision","lit", "chaise", "canapé", "table", "garde-robe"]
class_names +=["abeille", "scarabée", "papillon", "chenille", "cafard","ours", "léopard", "lion", "tigre", "loup","pont", "château", "maison", "route", "gratte-ciel","nuage", "forêt", "montagne", "plaine", "mer"]
class_names +=["chameau", "bétail", "chimpanzé", "éléphant", "kangourou","renard", "porc-épic", "opossum", "raton laveur", "moufette","crabe", "homard", "escargot", "araignée", "ver","bébé", "garçon", "fille", "homme", "femme"]
class_names +=["crocodile", "dinosaure", "lézard", "serpent", "tortue","hamster", "souris", "lapin", "musaraigne", "écureuil","érable", "chêne", "palmier", "pin", "saule","vélo", "autobus", "moto", "camionnette", "train","tondeuse à gazon", "fusée", "tramway", "réservoir", "tracteur"]
print("Cette image est un(e) : ", class_names[np.argmax(predictions)],predictions)
