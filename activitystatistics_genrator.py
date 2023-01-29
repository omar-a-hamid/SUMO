"""
dependncies / inputs: (outdated!)
{
edges.csv --> folder conating all edges (Nourhan Shafik script)
gen.csv --> school files
stats.json
Bstop_ref_id.csv
Bstop.csv
bus_lines.csv
}
outputs:
{
stat_file_genrated.stat.xml --> genrates statistics file pushing 
}

"""


import json
import csv
import xml.etree.ElementTree as ET
from random import *
import numpy as np
from scipy.stats import norm
  



def to_sec(hour):
    return int(hour*60*60)

factor = (2/4)
standard_div_workhours = 5

stats_json = open ('stats.json', "r")
  

data_json = json.loads(stats_json.read())


inhabitants             = data_json["inhabitants"]
inhabitants = str( round(int(inhabitants)*(1+(1-factor))))

households              = data_json["households"]
households = str( round(int(households)*(1+(1-factor))))

childrenAgeLimit        = data_json["childrenAgeLimit"]
retirementAgeLimit      = data_json["retirementAgeLimit"]
carRate                 = data_json["carRate"]
unemploymentRate        = data_json["unemploymentRate"]
footDistanceLimit       = data_json["footDistanceLimit"]
incomingTraffic         = data_json["incomingTraffic"]
outgoingTraffic         = data_json["outgoingTraffic"]
laborDemand             = data_json["laborDemand"]

carPreference           = data_json["carPreference"]
meanTimePerKmInCity     = data_json["meanTimePerKmInCity"]
freeTimeActivityRate    = data_json["freeTimeActivityRate"]
uniformRandomTraffic    = data_json["uniformRandomTraffic"]
departureVariation      = data_json["departureVariation"]

defualt_population      = data_json["defualt_population"]
defualt_work_pos        = data_json["defualt_work_pos"]

school_defualt_pos = data_json["school_defualt_pos"]
school_defualt_beginAge = data_json["school_defualt_beginAge"]
school_defualt_endAge = data_json["school_defualt_endAge"]
school_defualt_capacity = data_json["school_defualt_capacity"]
school_defualt_opening = data_json["school_defualt_opening"]
school_defualt_closing = data_json["school_defualt_closing"]


begin_age = []
end_age = []
people_Nbr = []

op_hours=[]
op_prop = []

cl_prop = []
cl_hours=[]

gates_edges = []
gates_pos =[]
gates_outgoing =[]
gates_incoming =[] 


for index in data_json['population']:
    begin_age.append(index['beginAge'])
    end_age.append(index['endAge'])
    people_Nbr.append(index['peopleNbr'])


for index in data_json['opening']:
    op_prop.append(index['proportion'])
    op_hours.append(index['hour'])

for index in data_json['closing']:
    cl_hours.append(index['hour'])
    cl_prop.append(index['proportion'])

for index in data_json['gates']:
    gates_edges.append(index['edge'])
    gates_pos.append(index['pos'])
    gates_outgoing.append(index['incoming'])
    gates_incoming.append(index['outgoing'])


stats_json.close()



data_file = open('edges_float.csv','r')
reader = csv.reader(data_file, dialect='excel' )
counter = 0
ids_list = []

for row in reader:
    if(not (counter)):
        counter +=1
        continue

    id = row[0]
    ids_list.append(id)

data_file.close()


data_file_schools = open('gen_float.csv','r')
reader_schools = csv.reader(data_file_schools, dialect='excel' )
counter = 0
school_ids = []
school_edges = []


for row in reader_schools:
    if(not (counter)):
        counter +=1
        continue
        
    # print(row[6])

    school_ids.append(row[0])
    school_edges.append(row[-1])

data_file_schools.close()


##ref_id dectionary
ref_id_dect = {}
data_file_bstops_ref_id = open('Bstop_ref_id.csv','r')
reader_Bstops_refId = csv.reader(data_file_bstops_ref_id, dialect='excel' )
for row in reader_Bstops_refId:
    ref_id_dect[str(row[0])] = row[-1]

data_file_bstops_ref_id.close()

##bus stops
data_file_bstops = open('Bstop.csv','r')
reader_Bstops = csv.reader(data_file_bstops, dialect='excel' )
counter = 0
stops_ids = []
stops_edges = []
stops_pos = []


for row in reader_Bstops:
    if(not (counter)):
        counter +=1
        continue

    stops_ids.append(ref_id_dect[str(row[0])])
    stops_edges.append(row[1])
    stops_pos.append(str(round((float(row[2])+float(row[3]))/2)))


data_file_bstops.close()


##bus lines
data_file_Blines = open('bus_lines.csv','r')
reader_Blines = csv.reader(data_file_Blines, dialect='excel' )
counter = 0


Blines_data=[]
Blines_rouets=[]
for row in reader_Blines:
    if(not (counter)):
        counter +=1
        continue
        
    Blines_rouets.append(row[0])
    for element in row[2:]: 
        if(element):
           

            Blines_rouets.append(ref_id_dect[str(element)])


    Blines_data.append(Blines_rouets.copy())
    Blines_rouets.clear()
    print(Blines_data)


data_file_Blines.close()

statistics_file = open('stat_file_generated.stat.xml','w')


statistics_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
statistics_file.write('\n')
statistics_file.write('\n')
statistics_file.write('<city>\n')
statistics_file.write('	<general inhabitants="'+inhabitants+'" households="'+households+'" childrenAgeLimit="'+childrenAgeLimit+'" retirementAgeLimit="'+retirementAgeLimit+'" carRate="'+carRate+'" unemploymentRate="'+unemploymentRate+'" footDistanceLimit="'+footDistanceLimit+'" incomingTraffic="'+incomingTraffic+'" outgoingTraffic="'+outgoingTraffic+'" laborDemand="'+laborDemand+'"/>\n')
statistics_file.write('	<parameters carPreference="'+carPreference+'" meanTimePerKmInCity="'+meanTimePerKmInCity+'" freeTimeActivityRate="'+freeTimeActivityRate+'" uniformRandomTraffic="'+uniformRandomTraffic+'" departureVariation="'+departureVariation+'" />\n')
statistics_file.write('	\n')
statistics_file.write('	<population>\n') #insert poopulation here.. 
for beginAge, endAge, nbr in zip(begin_age,end_age,people_Nbr):

    statistics_file.write('		<bracket beginAge="'+beginAge+'" endAge="'+endAge+'" peopleNbr="'+nbr+'" />\n')


statistics_file.write('	</population>\n')
statistics_file.write('	\n')
statistics_file.write('	<workHours>\n')

temp = np.arange(0, 23,1)
  
proprtion_list = norm.pdf(temp, 14,standard_div_workhours)  


for hour, proprtion in zip(op_hours,op_prop):
    statistics_file.write('		<opening hour="'+hour+'" proportion="'+str(round(float(proprtion)*factor,2))+'" />\n')


for hour,proprtion_dash in zip(range(0,23),proprtion_list):
    statistics_file.write('		<opening hour="'+str(to_sec(hour))+'" proportion="'+str(round(float(proprtion_dash)*(1-factor),2))+'" />\n')
for hour, proprtion in zip(cl_hours,cl_prop):
    statistics_file.write('		<closing hour="'+hour+'" proportion="'+str(round(float(proprtion)*factor,2))+'" />\n')
for hour,proprtion_dash in zip(range(0,23),proprtion_list):
    statistics_file.write('		<closing hour="'+str(to_sec(hour))+'" proportion="'+str(round(float(proprtion_dash)*(1-factor),2))+'" />\n')
statistics_file.write('	</workHours>\n')
statistics_file.write('	\n')
statistics_file.write('	<streets>\n')
for id in ids_list:

            statistics_file.write('		<street edge="'+str(id)+'" population="'+str(int(defualt_population)+randint(1,5))+'" workPosition="'+str(int(defualt_work_pos)+randint(1,5))+'" />\n')

statistics_file.write('	</streets>\n')
statistics_file.write('	\n')

statistics_file.write('	<cityGates>\n')
for gate_edge,gate_pos,gate_incoming,gate_outgoing in zip(gates_edges,gates_pos,gates_incoming,gates_outgoing):

    statistics_file.write('		<entrance edge="'+gate_edge+'" pos="'+gate_pos+'" incoming="'+gate_incoming+'" outgoing="'+gate_outgoing+'" />\n')

statistics_file.write('	</cityGates>\n')
statistics_file.write('	\n')


statistics_file.write('	<schools>\n') # only eges are genrated, maybe defualt values for the rest? # TODO

for school_edge,school_id in zip(school_edges,school_ids):
		statistics_file.write('		<school edge="'+school_edge+'" pos="'+school_defualt_pos+'" beginAge="'+school_defualt_beginAge+'" endAge="'+school_defualt_endAge+'" capacity="'+school_defualt_capacity+'" opening="'+school_defualt_opening+'" closing="'+school_defualt_closing+'" />\n')
statistics_file.write('	</schools>\n')
statistics_file.write('	\n')



statistics_file.write('	<busStations>\n')
for stop_id,stop_edge,stop_pos in zip(stops_ids,stops_edges,stops_pos):
		statistics_file.write('		<busStation id="'+stop_id+'" edge="'+stop_edge+'" pos="'+stop_pos+'" />\n')
statistics_file.write('	</busStations>\n')
statistics_file.write('	\n')
statistics_file.write('	<busLines>\n')


base_rate = round(int(inhabitants)/50) # TODO hardcodded 


for line in Blines_data:

    statistics_file.write('		<busLine id="'+line[0]+'" maxTripDuration="'+str(randint(5,15))+'">\n') #TODO: max trip duration # TODO hardcoded
    statistics_file.write('			<stations>\n')

    for stops in line[2:]:
        statistics_file.write('				<station refId="'+stops+'" />\n')
    statistics_file.write('			</stations>\n')
    statistics_file.write('			<revStations>\n')
    for stops in reversed(line[2:]):
        statistics_file.write('				<station refId="'+stops+'" />\n')

    const_rand_1 = randint(0,3600)
    const_rand_2 = randint(0,3600)
    const_rand_3= randint(0,3600)
    const_rand_4 = randint(0,3600)
    statistics_file.write('			</revStations>\n')
    statistics_file.write('			<frequencies>\n') #TODO: mange frequncies
    statistics_file.write('				<frequency begin="'+str(to_sec(5)+const_rand_1)+'" end="'+str(to_sec(8)+const_rand_2)+'" rate="'+str(base_rate*2+randint(0,base_rate))+'" />\n') #TODO
    statistics_file.write('				<frequency begin="'+str(to_sec(8)+const_rand_2)+'" end="'+str(to_sec(18)+const_rand_3)+'" rate="'+str(base_rate*5+randint(0,base_rate))+'" />\n')
    statistics_file.write('				<frequency begin="'+str(to_sec(18)+const_rand_3)+'" end="'+str(to_sec(21)+const_rand_4)+'" rate="'+str(base_rate*4+randint(0,base_rate))+'" />\n')
    statistics_file.write('				<frequency begin="'+str(to_sec(21)+const_rand_4)+'" end="'+str(to_sec(22)+const_rand_1)+'" rate="'+str(base_rate*1+randint(0,base_rate))+'" />\n')
    statistics_file.write('			</frequencies>\n')
    statistics_file.write('		</busLine>\n')
    statistics_file.write('		\n')

statistics_file.write('	</busLines>\n')
statistics_file.write('	\n')
statistics_file.write('</city>')

"""    statistics_file.write('				<frequency begin="21600" end="36000" rate="300" />\n') #TODO
    statistics_file.write('				<frequency begin="36000" end="57600" rate="1800" />\n')
    statistics_file.write('				<frequency begin="57600" end="68400" rate="300" />\n')
    statistics_file.write('				<frequency begin="68400" end="86399" rate="1800" />\n')
    """


"""

5+l->8+x low factor 2   20-> 40
8+x->6+y Vhigh factor 5 -> 100
6+y->9+z high  factor 4 --> 80 
9+z->12 Vlow factor 1  --> 20 

"""