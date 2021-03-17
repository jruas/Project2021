
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

filename='IrisData.csv'

with open (filename, 'rt') as csvFile:                              #[REFA]: code in "Me Messing up with CSV File" from week 7 of Programming and Scripting Module                  
    csvReader = csv.reader(csvFile, delimiter=',')
    firstLine= True                                                 # This is just to not print the first line of the csv file
    for line in csvReader:
        if firstLine:
            firstLine=False
            continue
        print (line)