#Analysis of Iris Fisher Dataset
#Author:Joana Ruas


import csv
import pandas as pd
import matplotlib.pyplot as plt 


#Iris Fisher Dataset downloaded in CSV and saved in project folder.                 [REF]: Dataset download: https://tableconvert.com/?output=csv
filename='IrisData.csv'

#Reading from CSV file     
with open (filename, 'rt') as csvFile:
    csvReader=csv.DictReader(csvFile)
    data={}                                         #defining an empty dict (data)
    for row in csvReader:                           #reading row by row
        for header, value in row.items():           #for each row read, appends the header and the correspondent value to the dict      #[REF]: https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
            try:
                data[header].append(value)          #Appending to the dict in this step
            except KeyError:
                data[header]=[value]


#Separating Dict Data into Lists. One list for each column. Data still as strings.
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
pd.set_option("display.precision", 2)                          #Change table to 2 decimal places [REF:https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html]                                    

#Describe function
#General Analysis
analysisPara=df.describe()                                         #analysis of parameters (count, mean, stf, min, max and percentiles)
#Analysis by species
setosaTBL=df.loc[0:49].describe()
versicolorTBL=df.loc[50:99].describe()
virginicaTBL=df.loc[100:].describe()

#Writing the info into the txt file:
textFile='VariablesSummary.txt'

def writeFile ():
    with open (textFile, "wt") as tf:
        tf.write('General Table'+ '\n' +'\n')
        tf.write(str(analysisPara) + '\n'+'\n')         #Values had to be converted to string. \n is for spacing between tables
        tf.write('Iris Setosa' + '\n' +'\n')
        tf.write(str(setosaTBL)+ '\n'+'\n')
        tf.write('Iris Vericolor' +'\n'+ '\n')
        tf.write(str(versicolorTBL)+'\n'+'\n')
        tf.write('Iris Virginica' + '\n'+ '\n')
        tf.write(str(virginicaTBL)+'\n'+'\n')

writeFile()


#HISTOGRAMS
#Separating each variable into the types of flowers.
#SEPAL LENGTH
setosaSL=sepalLength[:50]                                       #can eliminate this by using always like sepalLength[0:50]. It was easier to read this way, so left it like that
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


def generalHist():       
    #4 histograms in the same plot, for easier comparison                                                           
    bins=15
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)                      #[REF][16]: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

    ax0.hist(sepalLength, bins, histtype='bar', color="lightsteelblue")
    ax0.set_title('Sepal Length')

    ax1.hist(sepalWidth, bins, histtype='bar', color="lightsteelblue")
    ax1.set_title('Sepal Width')

    ax2.hist(petalLength, bins, histtype='bar', color="lightsteelblue")
    ax2.set_title('Petal Length')
    
    ax3.hist(petalWidth, bins, histtype='bar', color="lightsteelblue")
    ax3.set_title('Petal Width')

    fig.tight_layout()
    plt.savefig('generalHist.png')


def histFlower():
    bins=15

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

    # a line for each variable had to be created instead of code in comment to adjust transparencies for better reading.

    #ax0.hist(sepalLengthHist, bins, histtype='bar', color=colours, label=labels, stacked=True, edgecolor="grey")    
    #ax0.legend(prop={'size': 10})
    #ax0.set_title('Sepal Length')

    ax0.hist(setosaSL, bins=10, histtype="bar", color="goldenrod", label="Setosa", stacked=True, edgecolor="grey")                 #[REF][17]https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
    ax0.hist(virginicaSL, bins=10, histtype="bar", color="cornflowerblue", label="Virginica", stacked=True, edgecolor="grey")
    ax0.hist(versicolorSL, bins=10, histtype="bar", color="salmon", label="Versicolor", stacked=True, edgecolor="grey", alpha=0.6)
    ax0.legend(prop={"size":10})
    ax0.set_title('Sepal Length')

    ax1.hist(setosaSW, bins=10, histtype="bar", color="goldenrod", label="Setosa", stacked=True, edgecolor="grey")                 ##https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
    ax1.hist(virginicaSW, bins=10, histtype="bar", color="cornflowerblue", label="Virginica", stacked=True, edgecolor="grey")
    ax1.hist(versicolorSW, bins=10, histtype="bar", color="salmon", label="Versicolor", stacked=True, edgecolor="grey", alpha=0.6)
    ax1.legend(prop={"size":10})
    ax1.set_title('Sepal Width')

    ax2.hist(setosaPL, bins=5, histtype="bar", color="goldenrod", label="Setosa", stacked=True, edgecolor="grey")                 ##https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
    ax2.hist(virginicaPL, bins=5, histtype="bar", color="cornflowerblue", label="Virginica", stacked=True, edgecolor="grey")
    ax2.hist(versicolorPL, bins=5, histtype="bar", color="salmon", label="Versicolor", stacked=True, edgecolor="grey", alpha=0.6)
    ax2.legend(prop={"size":10})
    ax2.set_title('Petal Length')

    ax3.hist(setosaPW, bins=5, histtype="bar", color="goldenrod", label="Setosa", stacked=True, edgecolor="grey")                 ##https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
    ax3.hist(virginicaPW, bins=5, histtype="bar", color="cornflowerblue", label="Virginica", stacked=True, edgecolor="grey")
    ax3.hist(versicolorPW, bins=5, histtype="bar", color="salmon", label="Versicolor", stacked=True, edgecolor="grey", alpha=0.6)
    ax3.legend(prop={"size":10})
    ax3.set_title('Petal Width')

    fig.tight_layout()
    plt.savefig('4plots.png')
    #plt.show()

generalHist()
histFlower()

#SCATTER:
def scatterSepalLength():
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)

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

    plt.tight_layout()
    plt.savefig('ScatterSepalLength.png')

def scatterSepalWidth():
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
    ax0.scatter(sepalWidth[:50], setosaSL, color='goldenrod', label='Setosa')      #[REF] data colors: https://matplotlib.org/stable/gallery/color/named_colors.html
    ax0.scatter(sepalWidth[50:100], versicolorSL, color='salmon', label='Versicolor')
    ax0.scatter(sepalWidth[100:], virginicaSL, color='cornflowerblue', label='Virginica')
    ax0.set_xlabel('Sepal Width (cm)')                                                  #[REF] ax1.set_ylabel :https://stackoverflow.com/questions/6963035/pyplot-axes-labels-for-subplots
    ax0.set_ylabel('Setal Length (cm)')
    ax0.set_facecolor('ivory')                                                       #[REF] ax1.set_facecolor: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
    ax0.legend()                                                                    #[REF] ax1.legend() https://stackoverflow.com/questions/52056261/how-to-set-label-for-each-subplot-in-a-plot-in-matplotlib
    
    ax1.scatter(sepalWidth[:50], setosaPL, color='goldenrod', label='Setosa')
    ax1.scatter(sepalWidth[50:100], versicolorPL, color='salmon', label='Versicolor')
    ax1.scatter(sepalWidth[100:], virginicaPL, color='cornflowerblue', label='Virginica')
    ax1.set_xlabel('Sepal Width (cm)')
    ax1.set_ylabel('Petal Length (cm)')
    ax1.set_facecolor('ivory')
    ax1.legend()

    ax2.scatter(sepalWidth[:50], setosaPW, color='goldenrod', label='Setosa')
    ax2.scatter(sepalWidth[50:100], versicolorPW, color='salmon', label='Versicolor')
    ax2.scatter(sepalWidth[100:], virginicaPW, color='cornflowerblue', label='Virginica')
    ax2.set_xlabel('Sepal Width (cm)')
    ax2.set_ylabel('Petal Width (cm)')
    ax2.set_facecolor('ivory')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('ScatterSepalWidth.png')

def scatterPetalLength():
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)

    ax0.scatter(petalLength[:50], setosaSL, color='goldenrod', label='Setosa')
    ax0.scatter(petalLength[50:100], versicolorSL, color='salmon', label='Versicolor')
    ax0.scatter(petalLength[100:], virginicaSL, color='cornflowerblue', label='Virginica')
    ax0.set_xlabel('Petal Length (cm)')
    ax0.set_ylabel('Sepal Length (cm)')
    ax0.set_facecolor('ivory')
    ax0.legend()

    ax1.scatter(petalLength[:50], setosaSW, color='goldenrod', label='Setosa')
    ax1.scatter(petalLength[50:100], versicolorSW, color='salmon', label='Versicolor')
    ax1.scatter(petalLength[100:], virginicaSW, color='cornflowerblue', label='Virginica')
    ax1.set_xlabel('Petal Length (cm)')
    ax1.set_ylabel('Sepal Width (cm)')
    ax1.set_facecolor('ivory')
    ax1.legend()

    ax2.scatter(petalLength[:50], setosaPW, color='goldenrod', label='Setosa')
    ax2.scatter(petalLength[50:100], versicolorPW, color='salmon', label='Versicolor')
    ax2.scatter(petalLength[100:], virginicaPW, color='cornflowerblue', label='Virginica')
    ax2.set_xlabel('Petal Length (cm)')
    ax2.set_ylabel('Petal Width (cm)')
    ax2.set_facecolor('ivory')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('ScatterPetalLength.png')

def scatterPetalWidth():
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
    
    ax0.scatter(petalWidth[:50], setosaSL, color='goldenrod', label='Setosa')
    ax0.scatter(petalWidth[50:100], versicolorSL, color='salmon', label='Versicolor')
    ax0.scatter(petalWidth[100:], virginicaSL, color='cornflowerblue', label='Virginica')
    ax0.set_xlabel('Petal Width (cm)')
    ax0.set_ylabel('Sepal Length (cm)')
    ax0.set_facecolor('ivory')
    ax0.legend()

    ax1.scatter(petalWidth[:50], setosaSW, color='goldenrod', label='Setosa')
    ax1.scatter(petalWidth[50:100], versicolorSW, color='salmon', label='Versicolor')
    ax1.scatter(petalWidth[100:], virginicaSW, color='cornflowerblue', label='Virginica')
    ax1.set_xlabel('Petal Width (cm)')
    ax1.set_ylabel('Sepal Width (cm)')
    ax1.set_facecolor('ivory')
    ax1.legend()

    ax2.scatter(petalWidth[:50], setosaPL, color='goldenrod', label='Setosa')
    ax2.scatter(petalWidth[50:100], versicolorPL, color='salmon', label='Versicolor')
    ax2.scatter(petalWidth[100:], virginicaPL, color='cornflowerblue', label='Virginica')
    ax2.set_xlabel('Petal Width (cm)')
    ax2.set_ylabel('Petal Length (cm)')
    ax2.set_facecolor('ivory')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('ScatterPetalWidth.png')


scatterSepalLength()
scatterSepalWidth()
scatterPetalLength()
scatterPetalWidth()

