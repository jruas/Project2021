
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

