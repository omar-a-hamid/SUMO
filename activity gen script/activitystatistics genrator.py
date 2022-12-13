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

stats_json.close()

statistics_file = open('stat_file_generated.stat.xml','w')


statistics_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
statistics_file.write('\n')
statistics_file.write('\n')
statistics_file.write('<city>\n')
statistics_file.write('	<general inhabitants="'+inhabitants+'" households="'+households+'" childrenAgeLimit="'+childrenAgeLimit+'"etirementAgeLimit="'+retirementAgeLimit+'"arRate="'+carRate+'" unemploymentRate="'+unemploymentRate+'" footDistanceLimit="'+footDistanceLimit+'"incomingTraffic="'+incomingTraffic+'" outgoingTraffic="'+outgoingTraffic+'"laborDemand="'+laborDemand+'"/>\n')
statistics_file.write('	<parameters carPreference="'+carPreference+'" meanTimePerKmInCity="'+meanTimePerKmInCity+'" freeTimeActivityRate="'+freeTimeActivityRate+'" uniformRandomTraffic="'+uniformRandomTraffic+'" departureVariation="'+departureVariation+'" />\n')
statistics_file.write('	\n')
statistics_file.write('	<population>\n')
statistics_file.write('		<bracket beginAge="0" endAge="30" peopleNbr="30" />\n')
statistics_file.write('		<bracket beginAge="30" endAge="60" peopleNbr="40" />\n')
statistics_file.write('		<bracket beginAge="60" endAge="90" peopleNbr="30" />\n')
statistics_file.write('	</population>\n')
statistics_file.write('	\n')
statistics_file.write('	<workHours>\n')
statistics_file.write('		<opening hour="30600" proportion="0.30" />\n')
statistics_file.write('		<opening hour="32400" proportion="0.70" />\n')
statistics_file.write('		<closing hour="43200" proportion="0.20" />\n')
statistics_file.write('		<closing hour="63000" proportion="0.20" />\n')
statistics_file.write('		<closing hour="64800" proportion="0.60" />\n')
statistics_file.write('	</workHours>\n')
statistics_file.write('	\n')
statistics_file.write('	<streets>\n')
statistics_file.write('\n')
statistics_file.write('	</streets>\n')
statistics_file.write('	\n')
statistics_file.write('	<cityGates>\n')
statistics_file.write('		<entrance edge="-25584616#1" pos="1" incoming="0.5" outgoing="0.5" />\n')
statistics_file.write('		<!-- <entrance edge="e44t51" pos="280" incoming="0.5" outgoing="0.5" /> -->\n')
statistics_file.write('	</cityGates>\n')
statistics_file.write('	\n')
statistics_file.write('	<schools>\n')
statistics_file.write('	</schools>\n')
statistics_file.write('	\n')
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
statistics_file.write('</city>)\n')




""" root = ET.Element("Catalog")
    
m1 = ET.Element("mobile")
root.append (m1)
    
b1 = ET.SubElement(m1, "brand")
b1.text = "Redmi"
b2 = ET.SubElement(m1, "price")
b2.text = "6999"
    
m2 = ET.Element("mobile")
root.append (m2)
    
c1 = ET.SubElement(m2, "brand")
c1.text = "Samsung"
c2 = ET.SubElement(m2, "price")
c2.text = "9999"
    
m3 = ET.Element("mobile")
root.append (m3)
    
d1 = ET.SubElement(m3, "brand")
d1.text = "RealMe"
d2 = ET.SubElement(m3, "price")
d2.text = "11999"
    
tree = ET.ElementTree(root)
    
with open ("fileName.xml", "wb") as files :
    tree.write(files)
 """
""" a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)

 """