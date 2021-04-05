# Project2021

Project 2021 - Programming and Scripting GMIT
Author: Joana Ruas
Title: Fisher's Iris Dataset

-----------------------------------------------------------------------------------------------------------------------------
This is the background research prior to the analysis of the Fisher's Irish Dataset.

-----------------------------------------------------------------------------------------------------------------------------

## THE DATASET
The Irish Fisher dataset was developed by Ronal Fisher in 1936. The dataset consists in 50 samples of 4 parameters, for 3 flower species (Setosa, Versicolor and Virginica). The 4 parameters are Sepal Lenght, Speal Width, Petal Lenght and Petal Width. All parameters are in centimetres.
The combination of the four parameters, allowed Fisher to develope a linear discriminant model to distinguish the species from each other.
This dataset became a typical test case for many statistical classification techniques in machine learning. [REFA]

<img src="images/iris.png" width="100">

[REFB]
## WHY COLLECTING DATA?

## HOW DATA WERE COLLECTED?





## SUMMARY OF PROGRAM:
1. Download the fisher's iris data set to the project folder [REF1]
2. Converting the csv columns to lists
3. Convert list items from strings to floats
2. Summary of each variable to a single text file. 


## DETAILED STEPS OF PROGRAM:


## RESULTS




## REFERENCES:
[REFA]: https://en.wikipedia.org/wiki/Iris_flower_data_set
[REFB]: https://medium.com/@Nivitus./iris-flower-classification-machine-learning-d4e337140fa4
[REF1]: Dataset downloaded from https://tableconvert.com/?output=csv



# How to download the data set
Python code for download:
from sklearn import datasets
from sklearn.decomposition import PCA

iris=datasets.load_iris()

The dataset is saved as an array, lists formed by 4 elements.
