
#Importing Fisher Iris Dataset
#from sklearn import datasets
#from sklearn.decomposition import PCA

#iris=datasets.load_iris()

#print(type(iris))

#Saving dataset into a file.
#filename="irisdataset.txt"

#with open (filename, "wt") as f:
    #f.write('Hello')


#Reading the Iris Dataset from the csv file (in repository folder):

import csv
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

filename='IrisData.csv'

#with open (filename, 'rt') as csvFile:                              #[REFA]: code in "Me Messing up with CSV File" from week 7 of Programming and Scripting Module                  
    #csvReader = csv.reader(csvFile, delimiter=',')
    #firstLine= True                                                 # This is just to not print the first line of the csv file
    #for line in csvReader:
        #if firstLine:
         #   firstLine=False
          #  continue
        #print (line)

      
with open (filename, 'rt') as csvFile:
    csvReader=csv.DictReader(csvFile)
    data={}
    for row in csvReader:
        for header, value in row.items():                           #[REFB]: https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
            try:
                data[header].append(value)
            except KeyError:
                data[header]=[value]

#Lists created but in strings type. Data will be converted to float after
column1=data['ï»¿sepal_length']               
column2=data['sepal_width']              
column3=data['petal_length']
column4=data['petal_width']

#Converting List from string data to float data
sepalLength = []                                                    #[REFC]: https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
for item in column1:
    sepalLength.append(float(item))

sepalWidth=[]
for item in column2:
    sepalWidth.append(float(item))

petalLength=[]
for item in column3:
    petalLength.append(float(item))

petalWidth=[]
for item in column4:
    petalWidth.append(float(item))

#Creating Dict Lists                                                [REFD]: https://www.tutorialspoint.com/python_pandas/python_pandas_descriptive_statistics.htm
dictLists={'Sepal Length':pd.Series(sepalLength), 'Sepal Width':pd.Series(sepalWidth), 'Petal Length':pd.Series(petalLength), 'Petal Width':pd.Series(petalWidth)}

#Creating DataFrame                                                 [REFE]:https://www.w3resource.com/pandas/dataframe/dataframe-describe.php
df=pd.DataFrame(dictLists)                                          
analysisPara=df.describe()                  #analysis of parameters (count, mean, stf, min, max and percentiles)


#TRY TO SORT DECIMAL PLACES


#Writing the info into the txt file:
textFile='VariablesSummary.txt'

def writeFile ():
    with open (textFile, "wt") as tf:
        tf.write(str(analysisPara))

writeFile()


#Histogram for each variable 


#HISTOGRAMS
#SEPAL LENGTH
setosaSL=sepalLength[:50]
versicolorSL=sepalLength[50:100]
virginicaSL=sepalLength[100:]

#bins1=np.linspace(4,9,100)    #[REF]: https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib

#SEPAL WIDTH
setosaSW=sepalWidth[:50]
versicolorSW=sepalWidth[50:100]
virginicaSW=sepalWidth[100:]

#PETAL LENTGH
setosaPL=petalLength[:50]
versicolorPL=petalLength[50:100]
virginicaPL=petalLength[100:]

#PETAL WIDTH
setosaPW=petalWidth[:50]
versicolorPW=petalWidth[50:100]
virginicaPW=petalWidth[100:]

#
sepalLengthHist=[setosaSL, versicolorSL, virginicaSL]
sepalWidthHist=[setosaSW, versicolorSW, virginicaSW]
petalLengthHist=[setosaPL, versicolorPL, virginicaPL]
petalWidthHist=[setosaPW, versicolorPW, virginicaPW]

def generalHist():
    bins=15
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

    ax0.hist(sepalLength, bins, density=True, histtype='bar')
    ax0.set_title('Sepal Length')

    ax1.hist(sepalWidth, bins, density=True, histtype='bar', stacked=True)
    ax1.set_title('Sepal Width')

    ax2.hist(petalLength, bins, histtype='step', stacked=True, fill=False)
    ax2.set_title('Petal Length')
    
    ax3.hist(petalWidth, bins, histtype='bar')
    ax3.set_title('Petal Width')

    fig.tight_layout()
    plt.savefig('general Hist.png')




def histFlower():
    bins=15
    colors = ['red', 'tan', 'lime']
    colours=['red','blue','green']
    labels=['Setosa','Versicolor','Virginica']

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

    ax0.hist(sepalLengthHist, bins, density=True, histtype='bar', color=colours, label=labels)
    ax0.legend(prop={'size': 10})
    ax0.set_title('Sepal Length')

    ax1.hist(sepalWidthHist, bins, density=True, histtype='bar', color=colours, label=labels, stacked=True)
    ax1.set_title('Sepal Width')

    ax2.hist(petalLengthHist, bins, histtype='step', color=colours, label=labels, stacked=True, fill=False)
    ax2.set_title('Petal Length')
    # Make a multiple-histogram of data-sets with different length.
    ax3.hist(petalWidthHist, bins, histtype='bar', color=colours, label=labels)
    ax3.set_title('Petal Width')

    fig.tight_layout()
    plt.savefig('4plots.png')

generalHist()
histFlower()


