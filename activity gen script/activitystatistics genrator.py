"""
dependncies / inputs:
{
edges.csv --> folder conating all edges (Nourhan Shafik script)
gen.csv --> school files
stats.json
}
outputs:
{
stat_file_genrated.stat.xml --> genrates statistics file pushing 
}

"""

import json
import csv
import xml.etree.ElementTree as ET



stats_json = open ('stats.json', "r")
  

data_json = json.loads(stats_json.read())




inhabitants             = data_json["inhabitants"]
households              = data_json["households"]
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


""" 
for index in data_json['beginAge']:
    begin_age.append(index)

for index in data_json['endAge']:
    end_age.append(index)

for index in data_json['peopleNbr']:
    people_Nbr.append(index)
 """


stats_json.close()



data_file = open('edges_float.csv','r')



reader = csv.reader(data_file, dialect='excel' )
counter = 0
ids_list = []

for row in reader:
    if(not (counter)):
        counter +=1
        continue
        
    # print(row[6])
    id = row[0]
    # print(id)
    ids_list.append(id)


# print(ids_list)
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


# print(ids_list)
data_file_schools.close()

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
for hour, proprtion in zip(op_hours,op_prop):
    statistics_file.write('		<opening hour="'+hour+'" proportion="'+proprtion+'" />\n')

for hour, proprtion in zip(cl_hours,cl_prop):
    statistics_file.write('		<closing hour="'+hour+'" proportion="'+proprtion+'" />\n')

statistics_file.write('	</workHours>\n')
statistics_file.write('	\n')
statistics_file.write('	<streets>\n')
for id in ids_list:

            statistics_file.write('		<street edge="'+str(id)+'" population="'+defualt_population+'" workPosition="'+defualt_work_pos+'" />\n')

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

#from here not edited #TODO
statistics_file.write('	<busStations>\n')
statistics_file.write('		<busStation id="1" edge="-25584620#0" pos="10" />\n')
statistics_file.write('		<busStation id="2" edge="-25584621#0" pos="10" />\n')
statistics_file.write('		<busStation id="3" edge="-25584625#0" pos="10" />\n')
statistics_file.write('		<!-- <busStation id="4" edge="-25584629#0" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="5" edge="e24t23" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="6" edge="e23t33" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="7" edge="e33t32" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="8" edge="e32t31" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="9" edge="e31t21" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="10" edge="e21t11" pos="10" /> -->\n')
statistics_file.write('\n')
statistics_file.write('		<!-- <busStation id="101" edge="e12t11" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="102" edge="e13t12" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="103" edge="e14t13" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="104" edge="e24t14" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="105" edge="e23t24" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="106" edge="e33t23" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="107" edge="e32t33" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="108" edge="e31t32" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="109" edge="e21t31" pos="10" /> -->\n')
statistics_file.write('		<busStation id="110" edge="-25584626#0" pos="10" />\n')
statistics_file.write('\n')
statistics_file.write('		<busStation id="11" edge="-25584627#0" pos="10" />\n')
statistics_file.write('		<!-- <busStation id="12" edge="e22t32" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="13" edge="e32t42" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="14" edge="e42t41" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="15" edge="e41t31" pos="10" /> -->\n')
statistics_file.write('\n')
statistics_file.write('		<!-- <busStation id="111" edge="e22t12" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="112" edge="e32t22" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="113" edge="e42t32" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="114" edge="e41t42" pos="10" /> -->\n')
statistics_file.write('		<!-- <busStation id="115" edge="e31t41" pos="10" /> -->\n')
statistics_file.write('	</busStations>\n')
statistics_file.write('	\n')
statistics_file.write('	<busLines>\n')
statistics_file.write('		<busLine id="101" maxTripDuration="10">\n')
statistics_file.write('			<stations>\n')
statistics_file.write('				<station refId="1" />\n')
statistics_file.write('				<station refId="3" />\n')
statistics_file.write('				<!-- <station refId="4" /> -->\n')
statistics_file.write('				<!-- <station refId="5" /> -->\n')
statistics_file.write('				<!-- <station refId="6" /> -->\n')
statistics_file.write('				<!-- <station refId="7" /> -->\n')
statistics_file.write('				<!-- <station refId="8" /> -->\n')
statistics_file.write('				<!-- <station refId="9" /> -->\n')
statistics_file.write('			</stations>\n')
statistics_file.write('			<revStations>\n')
statistics_file.write('				<!-- <station refId="109" /> -->\n')
statistics_file.write('				<!-- <station refId="108" /> -->\n')
statistics_file.write('				<!-- <station refId="107" /> -->\n')
statistics_file.write('				<!-- <station refId="106" /> -->\n')
statistics_file.write('				<!-- <station refId="105" /> -->\n')
statistics_file.write('				<!-- <station refId="104" /> -->\n')
statistics_file.write('				<!-- <station refId="103" /> -->\n')
statistics_file.write('				<!-- <station refId="102" /> -->\n')
statistics_file.write('			</revStations>\n')
statistics_file.write('			<frequencies>\n')
statistics_file.write('				<frequency begin="21600" end="36000" rate="300" />\n')
statistics_file.write('				<frequency begin="36000" end="57600" rate="1800" />\n')
statistics_file.write('				<frequency begin="57600" end="68400" rate="300" />\n')
statistics_file.write('				<frequency begin="68400" end="86399" rate="1800" />\n')
statistics_file.write('			</frequencies>\n')
statistics_file.write('		</busLine>\n')
statistics_file.write('		\n')
statistics_file.write('		<busLine id="102" maxTripDuration="7">\n')
statistics_file.write('			<stations>\n')
statistics_file.write('				<!-- <station refId="15" /> -->\n')
statistics_file.write('				<!-- <station refId="9" /> -->\n')
statistics_file.write('				<!-- <station refId="10" /> -->\n')
statistics_file.write('				<!-- <station refId="1" /> -->\n')
statistics_file.write('				<!-- <station refId="11" /> -->\n')
statistics_file.write('				<!-- <station refId="12" /> -->\n')
statistics_file.write('				<!-- <station refId="13" /> -->\n')
statistics_file.write('				<!-- <station refId="14" /> -->\n')
statistics_file.write('			</stations>\n')
statistics_file.write('			<revStations>\n')
statistics_file.write('				<!-- <station refId="114" /> -->\n')
statistics_file.write('				<!-- <station refId="113" /> -->\n')
statistics_file.write('				<!-- <station refId="112" /> -->\n')
statistics_file.write('				<!-- <station refId="111" /> -->\n')
statistics_file.write('				<!-- <station refId="101" /> -->\n')
statistics_file.write('				<!-- <station refId="110" /> -->\n')
statistics_file.write('				<!-- <station refId="109" /> -->\n')
statistics_file.write('				<!-- <station refId="115" /> -->\n')
statistics_file.write('			</revStations>\n')
statistics_file.write('			<frequencies>\n')
statistics_file.write('				<frequency begin="28800" end="32400" rate="600" />\n')
statistics_file.write('				<frequency begin="57600" end="64800" rate="600" />\n')
statistics_file.write('			</frequencies>\n')
statistics_file.write('		</busLine>\n')
statistics_file.write('	</busLines>\n')
statistics_file.write('	\n')
statistics_file.write('</city>')

