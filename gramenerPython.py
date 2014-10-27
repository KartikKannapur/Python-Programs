#Program - Calculating the Median

import sys
import csv
import operator

#Display the contents of the CSV file
print open('salaries.csv').read()

data = csv.DictReader(open('salaries.csv','rb'))
data_values = sorted(data)

data_values_plumbers = {}
data_values_lawyers = {}
data_values_doctors = {}


for i in xrange(len(data_values)):
    if data_values[i].values()[2]=='Plumbers':
        data_values_plumbers[data_values[i].values()[1]]=data_values[i].values()[0]
data_values_plumbers = dict((k,int(v)) for k,v in data_values_plumbers.iteritems())
data_values_plumbers = data_values_plumbers.values()

for i in xrange(len(data_values)):
    if data_values[i].values()[2]=='Lawyers':
        data_values_lawyers[data_values[i].values()[1]]=data_values[i].values()[0]
data_values_lawyers = dict((k,int(v)) for k,v in data_values_lawyers.iteritems())
data_values_lawyers = data_values_lawyers.values()

for i in xrange(len(data_values)):
    if data_values[i].values()[2]=='Doctors':
        data_values_doctors[data_values[i].values()[1]]=data_values[i].values()[0]
data_values_doctors = dict((k,int(v)) for k,v in data_values_doctors.iteritems())
data_values_doctors = data_values_doctors.values()


print "Plumbers ",sorted(data_values_plumbers)[len(data_values_plumbers)//2]
print "Lawyers ",sorted(data_values_lawyers)[len(data_values_lawyers)//2]
print "Doctors ",sorted(data_values_doctors)[len(data_values_doctors)//2]
