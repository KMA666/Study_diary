import folium, os, pandas as pd
from folium.plugins import HeatMap

sanMap = folium.Map(location=[37.76, -122.42], zoom_start=14)
cdata = pd.read_csv(r"C:\Users\yanha\Downloads\CrimeData2016 (1).csv")
heatData = cdata[['Y', 'X']].values.tolist()
HeatMap(heatData).add_to(sanMap)
sanMap.save("san_map_严浩睿20240395.html")
os.system("explorer san_map.html")