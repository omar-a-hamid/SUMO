import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

tree=et.parse('osm_ptlines.xml')
root=tree.getroot()



# print(root[1])

# root=tree.getroot()
# print(root.attrib)

# root=tree.getroot()
# root=tree.getroot()


# root=tree.getroot()
# print(root.attrib)


lineDetails = []
moredetails=[]
sub = 'bus'
dictionary = {}
print("--------------------------------")
i = 0
index = 0
for line in root.iter('ptLine'):
	# print((line.attrib))
	# print(line.iter('id'))
	print((line.attrib.get('id')))#prints id of route 
	dictionary['line_id']=(line.attrib.get('id'))
	dictionary['length']=0
	# lineDetails.append((line.attrib.get('id')))
	for stop in line.iter('busStop'):
		
		# print(line.iter)
		print((stop.attrib.get('id')))#prints ids of line in the route
		dictionary[str(index)]=(stop.attrib.get('id'))
		# lineDetails.append((stop.attrib.get('id')))
		index=index+1
	lineDetails.append(dictionary.copy())
	dictionary['length']=str(index)
	print(dictionary)
	print(lineDetails)
	index = 0
	# dictionary.clear()
	

""" 
for line in root.iter('busStop'):
	i+=1
	# print(i)
	# print(poly.attrib.get('type') == sub)
	# print(line.iter('id'))
	# print(line.attrib)

	try: 
		# print(child[0])
		print((line.attrib))
		lineDetails.append((line.attrib))

		if sub in (line.attrib.get('type')):
			# print(line.attrib.get('id'))
			# lineDetails.append(line.attrib.get('id'))
			# lineDetails.append(line.attrib)
			# lineDetails.append(line[0].attrib)

			# moredetails.append(line[0].attrib.get('edges'))
			# print(poly.attrib)
			pass
		# print((poly.attrib.get('id')))

			# np.average()
			# print(average(poly.attrib.get('shape'), axis=0))
		pass

	except: 
		continue 
 """
print(lineDetails)
df = pd.DataFrame.from_dict(lineDetails) 


df.to_csv (r'bus_lines.csv', index = False, header=True)


