from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression   #Algoritmo de regresion lineal

boston = load_boston()  #Asignacion del dataset
print("\n", boston.keys(), "\n")    #Keywords del dataset

print(boston.target.shape, "\n")

X_train, X_test, Y_train, Y_test = train_test_split(boston.data, boston.target)

print(Y_test.shape,"\n")

lr = LinearRegression() #Asignacion del algoritmo

lr.fit(X_train, Y_train)    #Entrenamiento

print(boston['feature_names'], "\n")    #Tipos de datos

print(boston['DESCR'], "\n")    #Descripcion del dataset

print(lr.score(X_test, Y_test),"\n")    #Porcentaje de aciertos