import folium
import pandas as pd

def get_volcano_color(m) :
    if m > 3000 :
        return "red"
    elif m > 1000 :
        return "orange"
    return "green"

# import volcano locations
volcanoes = pd.read_csv(r"app2_webmap\resources\Volcanoes.txt")

# Get longitude, latitude, and names from volcanoes dataframe
longitude=list(volcanoes["LON"])
latitude=list(volcanoes["LAT"])
names=list(volcanoes["NAME"])
elev=list(volcanoes["ELEV"])

# zip up the coordinates, then zip up with names and elevations
coordinates=zip(latitude,longitude)
coor_names=zip(coordinates,names,elev)
#[print(x,y) for x,y in coor_names]

# create html query frame for Volcanoes
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# create folium map object
map = folium.Map(location=[latitude[0], longitude[0]], zoom_start=5, tiles="Mapbox Bright")

# Add markers to map
fg1=folium.FeatureGroup(name="Volcanoes")
for x, y, z in coor_names:
    iframe = folium.IFrame(html=html %(y,y,z), width=200, height=75)
    fg1.add_child(folium.Circle(location=x, popup=folium.Popup(iframe), radius=5000,
    fill_color=get_volcano_color(z), fill=True, fill_opacity=0.7, color = "black"))
    #fg.add_child(folium.Marker(location=x, popup=folium.Popup(iframe), icon= folium.Icon(color=get_volcano_color(z),icon='mountain')))


# add folium layer from GeoJson data
fg2=folium.FeatureGroup(name="Populations")
fg2.add_child(folium.GeoJson(data=open(r"app2_webmap\resources\world.json","r",encoding="utf-8-sig").read(),
style_function=(lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"})))

# add feature groups to map as well as a layer control
map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl(position="topright",collapsed=True))

# save to html
map.save("app2_webmap\Map1.html")
