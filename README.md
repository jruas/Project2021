# Project2021

Project 2021 - Programming and Scripting GMIT
Author: Joana Ruas
Title: Fisher's Iris Dataset

-----------------------------------------------------------------------------------------------------------------------------
This is the background research prior to the analysis of the Fisher's Irish Dataset.

-----------------------------------------------------------------------------------------------------------------------------

## THE Iris Fisher
The Iris Fisher dataset was developed by Ronal Fisher in 1936. The dataset consists in 50 samples of 4 parameters, for 3 flower species (Setosa, Versicolor and Virginica). The 4 parameters are Sepal Lenght, Speal Width, Petal Lenght and Petal Width. All parameters are in centimetres.
The combination of the four parameters, allowed Fisher to develope a linear discriminant model to distinguish the species from each other.
This dataset became a typical test case for many statistical classification techniques in machine learning. [A]

<img src="images/Iris.PNG" width="800">

[B]

The data Ronal Risher used, were collected by the botanist Dr.Edgar Anderson and published in 1935. Anderson collected data from Iris Setosa and Iris Versicolor from Gaspe Peninsula, Canada. To make the data collection as accurate as possible, all samples were "from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus". For the Iris Virginica, the same rigor was applied to the collection. Anderson was a student in Washington University in St.Luis in 1929, when he took a fellowship to work in Britain with other scientists. One of these scientists was Ronal Fisher, who obtained Anderson's permission to use the data in the article (xxxx) in 1936: The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics. [A,C]


## why STIL IMPORTANT TODAY?


## Goal of this research:
- Analysis data and identify the three species of Iris, based on that data analysis.


# Analysis of variables
The first step to understand the database was to evaluate the classic statistic parameters (number of samples, minumum and maximum values, average, standard deviation and percentils). This was the table obtained that summarizes the data for the 4 measures: Sepal Lenght, Sepal Width, Petal Length and Petal Width:
<img src="images/generaltable.png" width="500">




## STEP in PROGRAM FILE:
1. Download the fisher's iris data set to the project folder [1]
2. Converting the csv columns to lists of floats
3. Summary of each variable to a single text file. 


## DETAILED STEPS OF PROGRAM:




## RESULTS




## REFERENCES:
[A]: https://en.wikipedia.org/wiki/Iris_flower_data_set
[B]: https://medium.com/@Nivitus./iris-flower-classification-machine-learning-d4e337140fa4
[C]: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
[1]: Dataset downloaded from https://tableconvert.com/?output=csv



# How to download the data set
Python code for download:
from sklearn import datasets
from sklearn.decomposition import PCA

iris=datasets.load_iris()

The dataset is saved as an array, lists formed by 4 elements.
