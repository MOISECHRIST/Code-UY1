import h5py

#Lecture des données d'apprentissage et de test
def load_data():
    train_dataset = h5py.File('trainset.hdf5', "r")
    X_train = train_dataset["X_train"][:]
    y_train = train_dataset["Y_train"][:] 

    test_dataset = h5py.File('testset.hdf5', "r")
    X_test = test_dataset["X_test"][:]
    y_test = test_dataset["Y_test"][:] 
    
    return X_train, y_train, X_test, y_test