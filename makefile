SHELL=cmd.exe
.SHELLFLAGS = /c

route_file.rou.xml: stat_file_generated.stat.xml

stat_file_generated.stat.xml: stats.json edges_float.csv gen_float.csv Bstop_ref_id.csv Bstop.csv bus_lines.csv

	python activitystatistics_genrator.py
	.\activGen.cmd


Bstop_ref_id.csv: Bstop.csv

	python Bstops_ref.py

Bstop.csv: ../osm_stops.add.xml

	python parseBstop.py


gen_float.csv: gen.csv edges.csv

	python nearest_Edge.py
edges_float.csv: gen.csv edges.csv

	python nearestEdge.py


edges.csv: ../osm.net.xml
	python parsedge.py

bus_lines.csv: ../osm_ptlines.xml
	python bus_routes_parse_xml.py

gen.csv: ../osm.poly.xml
	python parse_xml.py