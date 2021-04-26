from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris #Dataset de medidas fisicas de flores tipo Iris
from sklearn.model_selection import train_test_split  #Funcion para division de datos
from sklearn.tree import export_graphviz #Modulo para graficacion del diagrama
import graphviz
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()  #Asignacion del dataset

X_train, X_test, Y_train, Y_test = train_test_split(iris.data, iris.target) #Division de datos de entrenamiento y datos de prueba

tree = DecisionTreeClassifier()

tree.fit(X_train, Y_train) #Entrenamiento del modelo

print(tree.score(X_test, Y_test)) #Impresion del puntuaje de entrenamiento

print(tree.score(X_train, Y_train)) #Imresion del puntuaje de prueba

export_graphviz(tree, out_file='tree.dot', class_names=iris.target_names, feature_names=iris.feature_names, impurity=False, filled=True)

with open('tree.dot') as f:
    dot_graph=f.read()

graphviz.Source(dot_graph) #Graficacion del diagrama de arbol