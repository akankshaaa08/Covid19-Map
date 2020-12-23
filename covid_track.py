import folium
import pandas as pd
import requests

map = folium.Map(location = [21.23212,81.668635] , zoom_start=5 , tiles="Stamen Terrain")   #default location
loc = pd.read_csv("India.csv")
geo = 'india_states.geojson'

def color_t(n) :        #compares total number of cases of each region
    if n < 1000 :
        return 'green'
    elif 1000 <= n < 5000 :
        return 'orange'
    else :
        return 'red'

total_cases = loc[['state','total']]

fg = folium.FeatureGroup(name="Total Cases")

for lt , lon , state ,total ,recover , death in zip( loc['lat'] , 
loc['lng'] , loc['state'] , loc['total'] , loc['recover'] , loc['death']) :
    iframe = state + "\nTotal: {}".format(total) + "\nRecovered: {} ".format(recover) + "\nDeaths: {} ".format(death) 
    fg.add_child(folium.Marker(location=[lt,lon] , popup=folium.Popup(iframe), icon=folium.Icon(color= color_t(total) ) ))

fg.add_child(folium.GeoJson(data=open('india_states.geojson','r' , encoding='utf-8-sig').read()))
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("COVID19-India.html")