#Analysis of Iris Fisher Dataset
#Author:Joana Ruas



import csv
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#Iris Fisher Dataset downloaded in CSV and saved in project folder. [REF]: Dataset download: https://tableconvert.com/?output=csv
filename='IrisData.csv'

#Reading from CSV file     
with open (filename, 'rt') as csvFile:
    csvReader=csv.DictReader(csvFile)
    data={}
    for row in csvReader:
        for header, value in row.items():                           #[REFB]: https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
            try:
                data[header].append(value)
            except KeyError:
                data[header]=[value]

#Lists created but in strings type. 
#Data will be converted to float in the next step
column1=data['ï»¿sepal_length']               
column2=data['sepal_width']              
column3=data['petal_length']
column4=data['petal_width']

#Converting Lists from string data to float numbers
sepalLength=[float(i) for i in column1]                             #[REF]:https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
sepalWidth=[float(i) for i in column2]
petalLength=[float(i) for i in column3]
petalWidth=[float(i) for i in column4]

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


#HISTOGRAMS
#Separating each variable into the types of flowers.
#SEPAL LENGTH
setosaSL=sepalLength[:50]                                       #can eliminate this by using always like sepalLength[0:50]
versicolorSL=sepalLength[50:100]
virginicaSL=sepalLength[100:]

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

#Combining Lists to be able to identiy data into plots
sepalLengthHist=[setosaSL, versicolorSL, virginicaSL]
sepalWidthHist=[setosaSW, versicolorSW, virginicaSW]
petalLengthHist=[setosaPL, versicolorPL, virginicaPL]
petalWidthHist=[setosaPW, versicolorPW, virginicaPW]

def generalHist():                                                                  #get source for subplots
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
    colours=['goldenrod','salmon','cornflowerblue']
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

#generalHist()
#histFlower()

#SCATTER:
def scatterFlowers ():
    
    fig, ((ax0, ax1, ax2),(ax3, ax4, ax5)) = plt.subplots(nrows=2, ncols=3)

    ax0.scatter(sepalLength[:50], setosaSW, color='goldenrod', label='Setosa')      #[REF] data colors: https://matplotlib.org/stable/gallery/color/named_colors.html
    ax0.scatter(sepalLength[50:100], versicolorSW, color='salmon', label='Versicolor')
    ax0.scatter(sepalLength[100:], virginicaSW, color='cornflowerblue', label='Virginica')
    ax0.set_xlabel('Sepal Length (cm)')                                                  #[REF] ax1.set_ylabel :https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    ax0.set_ylabel('Sepal Width (cm)')
    ax0.set_facecolor('ivory')                                                       #[REF] ax1.set_facecolor: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
    ax0.legend()                                                                    #[REF] ax1.legend() https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib
    
    ax1.scatter(sepalLength[:50], setosaPL, color='goldenrod', label='Setosa')
    ax1.scatter(sepalLength[50:100], versicolorPL, color='salmon', label='Versicolor')
    ax1.scatter(sepalLength[100:], virginicaPL, color='cornflowerblue', label='Virginica')
    ax1.set_xlabel('Sepal Length (cm)')
    ax1.set_ylabel('Petal Length (cm)')
    ax1.set_facecolor('ivory')
    ax1.legend()

    ax2.scatter(sepalLength[:50], setosaPW, color='goldenrod', label='Setosa')
    ax2.scatter(sepalLength[50:100], versicolorPW, color='salmon', label='Versicolor')
    ax2.scatter(sepalLength[100:], virginicaPW, color='cornflowerblue', label='Virginica')
    ax2.set_xlabel('Sepal Length (cm)')
    ax2.set_ylabel('Petal Length (cm)')
    ax2.set_facecolor('ivory')
    ax2.legend()

    ax3.scatter(sepalWidth[:50], setosaSL, color='goldenrod', label='Setosa')      #[REF] data colors: https://matplotlib.org/stable/gallery/color/named_colors.html
    ax3.scatter(sepalWidth[50:100], versicolorSL, color='salmon', label='Versicolor')
    ax3.scatter(sepalWidth[100:], virginicaSL, color='cornflowerblue', label='Virginica')
    ax3.set_xlabel('Sepal Width (cm)')                                                  #[REF] ax1.set_ylabel :https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    ax3.set_ylabel('Setal Length (cm)')
    ax3.set_facecolor('ivory')                                                       #[REF] ax1.set_facecolor: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
    ax3.legend()                                                                    #[REF] ax1.legend() https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib
    
    ax4.scatter(sepalWidth[:50], setosaPL, color='goldenrod', label='Setosa')
    ax4.scatter(sepalWidth[50:100], versicolorPL, color='salmon', label='Versicolor')
    ax4.scatter(sepalWidth[100:], virginicaPL, color='cornflowerblue', label='Virginica')
    ax4.set_xlabel('Sepal Width (cm)')
    ax4.set_ylabel('Petal Length (cm)')
    ax4.set_facecolor('ivory')
    ax4.legend()

    ax5.scatter(sepalWidth[:50], setosaPW, color='goldenrod', label='Setosa')
    ax5.scatter(sepalWidth[50:100], versicolorPW, color='salmon', label='Versicolor')
    ax5.scatter(sepalWidth[100:], virginicaPW, color='cornflowerblue', label='Virginica')
    ax5.set_xlabel('Sepal Width (cm)')
    ax5.set_ylabel('Petal Width (cm)')
    ax5.set_facecolor('ivory')
    ax5.legend()

    plt.show()

scatterFlowers()
