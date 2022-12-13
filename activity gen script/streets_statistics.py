"""
dependncies / inputs:
{
edges.csv --> folder conating all edges (Nourhan Shafik script)
stat_file.stat.xml --> folder conatining statistics report and needs streets to be added
}
outputs:
{
stat_file_edited.stat.xml --> updated statistics file pushing al edges with population and work postions
}

"""

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

