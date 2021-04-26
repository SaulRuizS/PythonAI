
import numpy as np
import sklearn
from sklearn.datasets import load_iris  #Dataset de medidas fisicas de flores tipo Iris
from sklearn.model_selection import train_test_split    #Funcion para division de datos

iris = load_iris()  #Asignacion del dataset
type (iris)

print("\n", iris.keys(), "\n")  #Keywords del dataset

X_train, X_test, Y_train, Y_test = train_test_split(iris['data'], iris['target'])   #Division de datos de entrenamiento y datos de prueba

print(X_train.shape, "\n")

print(Y_train.shape, "\n")

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=12)  #Asignacion del algoritmo KNN de clasificacion con 12 vecinos
knn.fit(X_train, Y_train)   #Entrenamiento

knn.score(X_test, Y_test)   #Porcentaje de aciertos

print(iris['feature_names'], "\n")  #Medidas de la flor

print(iris['target_names'], "\n")   #Nombre de la flor

#Algunas predicciones:
print(knn.predict([[4.1, 2.4, 3.3, 2.6]]))

print(knn.predict([[7.6, 3.8, 5.5, 4.4]]))

print(knn.predict([[5.1, 3.6, 1.9, 0.7]]))