#Program - Standard Deviations
import sys
import csv
import operator
import math

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


mean_plumbers = sum(data_values_plumbers)/len(data_values_plumbers)
mean_lawyers = sum(data_values_lawyers)/len(data_values_lawyers)
mean_doctors = sum(data_values_doctors)/len(data_values_doctors)

diff_plumbers = []
for i in range(len(data_values_plumbers)):
  diff_plumbers.append(data_values_plumbers[i]-mean_plumbers)

diff_plumbers_2 = [x*x for x in diff_plumbers]
SD_plumbers = math.sqrt(sum(diff_plumbers_2)/len(diff_plumbers_2))
#----#
diff_lawyers = []
for i in range(len(data_values_lawyers)):
  diff_lawyers.append(data_values_lawyers[i]-mean_lawyers)

diff_lawyers_2 = [x*x for x in diff_lawyers]
SD_lawyers = math.sqrt(sum(diff_lawyers_2)/len(diff_lawyers_2))
#----#
diff_doctors = []
for i in range(len(data_values_doctors)):
  diff_doctors.append(data_values_doctors[i]-mean_doctors)

diff_doctors_2 = [x*x for x in diff_doctors]
SD_doctors = math.sqrt(sum(diff_doctors_2)/len(diff_doctors_2))


print "Plumbers ",int(SD_plumbers)
print "Lawyers ",int(SD_lawyers)
print "Doctors ",int(SD_doctors)
