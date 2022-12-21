import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('osm.net.xml')
root=tree.getroot()

root=tree.getroot()
##print(root.iter('edge'))


polyDetails = []

#print("--------------------------------")
i = 0
for poly in root.iter('edge'):
	# i+=1
	# #print(i)
# 	# #print(poly.attrib.get('type') == sub)
	# try: 
	if (poly.attrib.get('shape')):
		#print(poly.attrib)
		polyDetails.append(poly.attrib)
# 			# np.average()
# 			# #print(average(poly.attrib.get('shape'), axis=0))

# 	except: 
# 		continue 



df = pd.DataFrame.from_dict(polyDetails) 
df = df.dropna(subset=['shape'])
df.to_csv (r'edges.csv', index = False, header=True)


print("Finish")