import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('../osm.net.xml')
root=tree.getroot()

root=tree.getroot()

polyDetails = []


i = 0
for poly in root.iter('edge'):

	if (poly.attrib.get('shape')):

		polyDetails.append(poly.attrib)


df = pd.DataFrame.from_dict(polyDetails) 
df = df.dropna(subset=['shape'])
df.to_csv (r'edges.csv', index = False, header=True)


print("Finish")