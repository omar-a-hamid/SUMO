import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('../osm.poly.xml')
root=tree.getroot()
print(root[2])

root=tree.getroot()
print(root.attrib)

root=tree.getroot()

polyDetails = []
sub = 'amenity.school'

print("--------------------------------")
i = 0
for poly in root:
	try: 
		if sub in (poly.attrib.get('type')):
			# print(poly.attrib)
			polyDetails.append(poly.attrib)
	except: 
		continue 





df = pd.DataFrame.from_dict(polyDetails) 

df = df.dropna(subset=['shape'])

# df.dropna( df,axis=0)

df.to_csv (r'gen.csv', index = False, header=True)


print("Finish")