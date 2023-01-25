import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('../osm_stops.add.xml')
root=tree.getroot()

root=tree.getroot()
print(root.iter('busStop'))


polyDetails = []

print("--------------------------------")
i = 0

for poly in root.iter('busStop'):

	if (poly.attrib.get('lane')):
		print(poly.attrib)
		polyDetails.append(poly.attrib)


df = pd.DataFrame.from_dict(polyDetails) 

edge = []
for i in df['lane']:
	temp = i.split('_')
	edge.append(temp[0])

df['lane'] = edge
df.rename(columns = {'lane':'edge'}, inplace = True)
df = df.drop(columns =['name', 'lines'])

print(df)

df.to_csv (r'Bstop.csv', index = False, header=True)

print("Finish")