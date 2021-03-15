
#Importing Fisher Iris Dataset
from sklearn.datasets import load_iris()
from sklearn.decomposition import PCA

iris=load_iris()
print(type(iris))

#Saving dataset into a file.
#filename="irisdataset.txt"

#with open (filename, "wt") as f:
    #f.write('Hello')