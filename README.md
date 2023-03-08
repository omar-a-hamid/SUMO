How to use: 

1-Load desired map from osmWebWizard (make sure to add transport lines)

    this will create a file containg the following files: 

        osm.net.xml
        osm.poly.xml
        osm.view.xml
        osm_pt.rou.xml
        osm_ptlines.xml
        osm_stops.add.xml
        stopinfos.xml
        trips.trips.xml
        trips_file.trips.rou.xml
        vehroutes.xml

2-Clone this repo in the same directory

3-edit "stats.json" for desired simulation parameters

4-run "sumo_route_genrator.cmd" or the makefile
    this willl run the following scripts:
        
        -parsedge.py
        -parse_xml.py
        -parseBstop.py
        -nearestEdge.py
        -bus_routes_parse_xml.py
        -Bstops_ref.py
        -activitystatistics_genrator.py

    then will  run the activityGen tool

    this will genrate the needed files 


5-open osm.sumocfg
    your simulation is ready to go!