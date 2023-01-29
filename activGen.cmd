
activitygen --net-file "../osm.net.xml" --stat-file stat_file_generated.stat.xml --output-file trips_file.trips.rou.xml --random


duarouter --net-file "../osm.net.xml" --route-files trips_file.trips.rou.xml --output-file "route_file.rou.xml" --ignore-errors true -W


duarouter -n "../osm.net.xml" -r "route_file.rou.xml" --ignore-errors --write-trips -o "../filtered.rou.xml"



@echo ^<?xml version=^"1.0^" encoding=^"UTF-8^"?^> > "../osm.sumocfg"
@echo. >> "../osm.sumocfg"
@echo ^<configuration xmlns:xsi=^"http://www.w3.org/2001/XMLSchema-instance^" xsi:noNamespaceSchemaLocation=^"http://sumo.dlr.de/xsd/sumoConfiguration.xsd^"^>  >> "../osm.sumocfg" 
@echo. >> "../osm.sumocfg"
@echo     ^<input^>  >> "../osm.sumocfg" 
@echo         ^<net-file value=^"osm.net.xml^"/^>  >> "../osm.sumocfg" 
@echo         ^<route-files value=^"filtered.rou.xml^"/^>  >> "../osm.sumocfg" 
@echo         ^<additional-files value=^"osm.poly.xml^"/^>  >> "../osm.sumocfg" 
@echo     ^</input^>  >> "../osm.sumocfg" 
@echo. >> "../osm.sumocfg"
@echo      ^<processing^>  >> "../osm.sumocfg" 
@echo          ^<ignore-route-errors value=^"true^"/^>  >> "../osm.sumocfg" 
@echo      ^</processing^>  >> "../osm.sumocfg" 
@echo. >> "../osm.sumocfg"
@echo      ^<routing^>  >> "../osm.sumocfg" 
@echo          ^<device.rerouting.adaptation-steps value=^"18^"/^>  >> "../osm.sumocfg" 
@echo          ^<device.rerouting.adaptation-interval value=^"10^"/^>  >> "../osm.sumocfg" 
@echo      ^</routing^>  >> "../osm.sumocfg"
@echo. >> "../osm.sumocfg" 
@echo      ^<report^>  >> "../osm.sumocfg" 
@echo          ^<verbose value=^"true^"/^>  >> "../osm.sumocfg" 
@echo          ^<duration-log.statistics value=^"true^"/^>  >> "../osm.sumocfg" 
@echo          ^<no-step-log value=^"true^"/^>  >> "../osm.sumocfg" 
@echo      ^</report^>  >> "../osm.sumocfg" 
@echo. >> "../osm.sumocfg"
@echo      ^<gui_only^>  >> "../osm.sumocfg" 
@echo          ^<gui-settings-file value=^"osm.view.xml^"/^>  >> "../osm.sumocfg" 
@echo      ^</gui_only^>  >> "../osm.sumocfg" 
@echo. >> "../osm.sumocfg"
@echo  ^</configuration^>  >> "../osm.sumocfg" 

echo.
echo.

echo complete

pause