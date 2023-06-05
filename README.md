# Assignment 3

## This notebook explores the ISS lightning data using 'pandas' and 'folium'


### What is ISS lightning data?

ISS lightning data refers to the information related to lightning events detected by instruments onboard the International Space Station (ISS). The ISS is equipped with instruments that can capture and record lightning activity from its vantage point in space.

The lightning data typically includes details such as the geographic location (latitude and longitude) where the lightning event occurred and the intensity of the lightning strike. This data can provide valuable insights into the distribution and characteristics of lightning activity across different regions.


#### The data has already been processed using the "netCDF4" & "xarray" libraries in a separate script.

The ".csv" contain only the following information about the global lightning strike data that has been extracted from the ".nc" files downloaded from "Earthdata" website: 

- file_name	
- latitude	
- longitude	
- orbit_start	
- orbit_end

The processed data in the ".csv" format has been used here to read and visualize it as webmap using [folium](https://python-visualization.github.io/folium/index.html "Link to the library") and the following specific function to create the map object:
- [folium.Map](https://python-visualization.github.io/folium/modules.html#module-folium.map)
- [folium.Marker](https://python-visualization.github.io/folium/quickstart.html#Markers)
- [folium.LayerControl](https://python-visualization.github.io/folium/modules.html#module-folium.features)

It provides a general overview of what folium looks like and how can you integrate data with geographical information with folium to produce colorful map objects. This is something we are looking forward to implement as a group for our final group work as well. 

p.s: most of the blocks below try to explain each process with the help of comments, but if anything is unclear feel free to contact the author of this notebook :D 
