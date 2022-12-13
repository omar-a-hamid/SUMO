import csv
import xml.etree.ElementTree as ET

defualt_population = "1"
defualt_work_pos = '1'


data_file = open('edges.csv','r')



reader = csv.reader(data_file, dialect='excel' )
counter = 0
ids_list = []

for row in reader:
    if(not (counter)):
        counter +=1
        continue
        
    # print(row[6])
    id = row[0]
    ids_list.append(id)


# print(ids_list)
data_file.close()

statistics_file = open('stat_file.stat.xml','r')
statistics_file_edited = open('stat_file_edited.stat.xml','w')

streets_flag = 0
for row in statistics_file:
    if(row.find('<streets>')!=-1):
        # statistics_file_edited.write(row)
        statistics_file_edited.write(row)
        streets_flag = 1
        continue
    elif(row.find('</streets>')!=-1):
        # statistics_file_edited.write(row)
        statistics_file_edited.write(row)
        streets_flag = 0
        continue

    if(streets_flag):
        # print(row)
        for id in ids_list:

            statistics_file_edited.write('		<street edge="'+str(id)+'" population="'+defualt_population+'" workPosition="'+defualt_work_pos+'" />\n')
            # print(id)
            # print('<street edge='+str(id)+' population='+defualt_population+' workPosition='+defualt_work_pos+' />')
        streets_flag = 0
        continue
    else:
        statistics_file_edited.write(row)


""" tree = ET.parse('stat_file.stat.xml')
root = tree.getroot()
print(root.findall('city'))
for street in root.findall('street'):
    print(street)
    rank = street.find('rank').text
    name = street.get('id')
    print(name, rank)
 """
# for child in root:
#     # print(child.tag)
#     for grand_child in child.iter:
#         print(grand_child)
    

# for rank in root.iter('streets'):
#     pass
    # print(rank.text)
    # new_rank = int(rank.text) + 1
    # rank.text = str(new_rank)
    # rank.set('updated', 'yes')

# tree.write('output.xml')

""" statistics_file = xml.etree.ElementTree.parse('stat_file.stat.xml')


new_tag = xml.etree.ElementTree.SubElement(statistics_file.getroot(), 'a')
new_tag.text = 'body text'
new_tag.attrib['x'] = '1' # must be str; cannot be an int
new_tag.attrib['y'] = 'abc'

# Write back to file
#et.write('file.xml')
statistics_file.write('stat _file_edited.stat.xml')

"""

""" streets_flag = 0
for row in statistics_file:
    if(row.find('<streets>')!=-1):
        streets_flag = 1
        continue
    elif(row.find('</streets>')!=-1):
        
        break

    if(streets_flag):
        print(row)
 """
""" 

import xml.etree.ElementTree

# Open original file
et = xml.etree.ElementTree.parse('file.xml')

# Append new tag: <a x='1' y='abc'>body text</a>
new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'a')
new_tag.text = 'body text'
new_tag.attrib['x'] = '1' # must be str; cannot be an int
new_tag.attrib['y'] = 'abc'

# Write back to file
#et.write('file.xml')
et.write('file_new.xml')


    for coordinates_pair in list_shapes:

        coordinates_pair_list =coordinates_pair.split(',')
        # print(coordinates_pair_list[0])

        # print ((coordinates_pair))
        # cords = map(float, coordinates_pair)
        # print (cords)
        x_cord.append(float(coordinates_pair_list[0]))
        y_cord.append(float(coordinates_pair_list[1]))
        # cord = map(float,coordinate)
        # print (cord)
        # print(coordinate)
    print(sum(x_cord)/len(x_cord),sum(y_cord)/len(y_cord))
    x_cord.clear()
    y_cord.clear()
 """