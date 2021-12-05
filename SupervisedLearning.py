import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=6)
iris = load_iris()
knn.fit(iris['data'], iris['target'])
knn.score((iris['data'], iris['target']))
