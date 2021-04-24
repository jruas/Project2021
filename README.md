# Project2021

Project 2021 - Programming and Scripting GMIT

Author: Joana Ruas

Title: Fisher's Iris Dataset

-----------------------------------------------------------------------------------------------------------------------------
GOAL:
Analysis data and identify the three species of Iris, based on that data analysis.

This is the background research prior to the analysis of the Fisher's Irish Dataset, and the analysis of results

-----------------------------------------------------------------------------------------------------------------------------
## Table of Contents

-[The Iris Fisher Dataset](#The-Iris-Fisher-Dataset)

-[Coding and Analysis of Results](#Coding-and-Analysis-of-Results)
    -[Modules used](#Modules-used)
    -[Reading from CSV](#Reading-from-CSV)
    
-[References](#References)

## The Iris Fisher Dataset
The Iris Fisher dataset was developed by Ronal Fisher in 1936. The dataset consists in 50 samples of 4 parameters, for 3 flower species (Setosa, Versicolor and Virginica). The 4 parameters are Sepal Lenght, Speal Width, Petal Lenght and Petal Width. All parameters are in centimetres.
The combination of the four parameters, allowed Fisher to develope a linear discriminant model to distinguish the species from each other.
This dataset became a typical test case for many statistical classification techniques in machine learning. [A]

<img src="images/Iris.PNG" width="600">

[B]

The data Ronal Risher used, were collected by the botanist Dr.Edgar Anderson and published in 1935. Anderson collected data from Iris Setosa and Iris Versicolor from Gaspe Peninsula, Canada. To make the data collection as accurate as possible, all samples were "from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus". For the Iris Virginica, the same rigor was applied to the collection. Anderson was a student in Washington University in St.Luis in 1929, when he took a fellowship to work in Britain with other scientists. One of these scientists was Ronal Fisher, who obtained Anderson's permission to use the data in the article (xxxx) in 1936: The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics. [A,C]


WHY STIL IMPORTANT TODAY?


## Coding and Analysis of Results
### Modules used:
To reach what was required in this project, it was necessary to import a few modules into Python:

<img src="images/modules.png" width="450">

**_CSV_** was the module imported to allow reading the csv file containing the Iris Fisher Dataset. The csv module implements classes to read and write tabular data in CSV format. [csv]

**_Pandas_** was the module imported to create a database with the variables exported from the csv file. As it will be explained below, it was the easier way to get the analysis of those variables, as Pandas has spefic functions for data analysis. Pandas is a module widely used for data science / data analytics. [pandas]

**_Matplotlib_** was the module imported for plotting the histograms and scatters required in the project. Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.[mat]

## Reading from CSV:
The dataset was downloaded in CSV format and saved in the project folder.[download] To read and access the data, this was the code used:

<img src="images/readingCSV.png" width="450">

An empty dict called data was defined, and then for each row of the CSV file, the header of the column and the respective value were appended do the dict.
The data exported from the CSV file was string type. For this analysis it was necessary to convert the data into floats. To convert all data into floats, keeping the info organized as per the CSV columns, it was used the code below, where the conversion was for done for each column in separate:

<img src="images/floatingData.png" width="450">

#

The first step to understand the database was to evaluate the classic statistic parameters (number of samples, minumum and maximum values, average, standard deviation and percentils). This was the table obtained that summarizes the data for the 4 measures: Sepal Lenght, Sepal Width, Petal Length and Petal Width (data in centimeters):


<img src="images/generaltable.png" width="500">

Each parameter was measured for the three species mentioned above. To evaluate each parameter in each species, detailed tables were generated:

<img src="images/detailed.png" width="900">

All the summary tables above can be found in the text file(VariablesSummary.txt) generated by the program (analysis.py) in the project folder. 
For an easier interpretation of data, histograms were developed. First, one histogram for each varaibles (disregarding the diferent species):


<img src="generalHist.png" width="450">
From the histograms above, it is possible to realize that the Sepal Length varies from 4 to 8 (aprox), the Sepal Width from 2 to 4.5 (aprox), the Petal Length from 1 to 7 (aprox) and the Petal Width from 0 t0 2.5 (aprox).
For this analysis, it was also developed the same histograms but showing the diferences between species within the same histogram. These histograms are below:

<img src="4plots.png" width="450">

Analysing the histograms above, it is possible to see that species Stosa has the minimum values of the data for Petal Length, Sepal Length and Speal Width, and maximum values of the data for Petal Width. It is also possible to see that the histogram for Virginica (in blue) is always a little to the right of histogram Versicolor (in red), which means for the 4 parameters it has in general bigger values. Virginica has also the maximum values for Sepal Lenght, Petal Lenght and Petal Width. 

For a better perception of the veriables' relationship, a scatter plot was developed combining each of the varibles with the others, and always speficifing the 3 species in each plot. These plots can be found in the picture below:

<img src="ScatterSepalLength.png" width="350">
<img src="ScatterSepalWidth.png" width="350">
<img src="ScatterPetalLength.png" width="350">
<img src="ScatterPetalWidth.png" width="350">

From the scatter plotos, the conclusion more easy to spot is that Setosa parameters always have very different values comparing with the other two species. It is possible to visualize in the 4 images above that the yellow dots are always more isolated.
While for the Virginica and Versicolor, although the two "patches" or values are always very close to each other, it is possible to see a well defined boundary between the two species. The only situation where both species have overlapping values in a more considerable way is in the plot Sepal Length vs Sepal Width.

## Summary of steps taken in [Analysis.py] :
1. Download the fisher's iris data set to the project folder [1]
2. Converting the csv columns to lists of floats
3. Summary of each variable to a single text file. 








## REFERENCES:
read me file:
https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
https://docs.github.com/pt/github/writing-on-github/basic-writing-and-formatting-syntax

Iris Fisher Dataset:
[A]: https://en.wikipedia.org/wiki/Iris_flower_data_set
[B]: https://medium.com/@Nivitus./iris-flower-classification-machine-learning-d4e337140fa4
[C]: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5


modules
csv: https://docs.python.org/3/library/csv.html
pandas: https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/
mat : https://matplotlib.org/

reading csv
download: [1]: Dataset downloaded from https://tableconvert.com/?output=csv




