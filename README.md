Project 2021 - Programming and Scripting GMIT
Author: Joana Ruas
Title: Fisher's Iris Dataset

-----------------------------------------------------------------------------------------------------------------------------
This is the background research prior to the analysis of the Fisher's Irish Dataset.

-----------------------------------------------------------------------------------------------------------------------------

SUMMARY


# Research
Multivariate dataset introduced by Ronal Fisher (1936).
Multiple measurements in taxonomic problems as an example of linear discriminant anaylysis.
Dataset consists of 50 samples from each of three species of Iris.
Four features were measures from each sample: length and width of the sepals and petals (cm).
Based on the combination of these four features Fisher developed a linear discriminant model to distinguish the species from each other. 

# How to download the data set
Python code for download:
from sklearn import datasets
from sklearn.decomposition import PCA

iris=datasets.load_iris()

The dataset is saved as an array, lists formed by 4 elements.

# Sava dataset in another document:
