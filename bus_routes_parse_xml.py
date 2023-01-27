import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('../osm_ptlines.xml')
root=tree.getroot()


lineDetails = []
moredetails=[]
sub = 'bus'
dictionary = {}
print("--------------------------------")
i = 0
index = 0
for line in root.iter('ptLine'):

	dictionary['line_id']=(line.attrib.get('id'))
	dictionary['length']=0

	for stop in line.iter('busStop'):

		dictionary[str(index)]=(stop.attrib.get('id'))
		index=index+1
		dictionary['length']=index
	lineDetails.append(dictionary.copy())
	dictionary.clear()

	index = 0


# print(lineDetails)

df = pd.DataFrame.from_dict(lineDetails) 
df.to_csv (r'bus_lines.csv', index = False, header=True)

print('finish')