import folium
import webbrowser

Map = folium.Map(
    location=[42.344252, 69.623823],
    zoom_start=15
)

folium.Circle(
    radius=100,
    location=[42.344252, 69.623823],
    color='crimson',
    fill=False,
).add_to(Map)

folium.CircleMarker(
    location=[42.344252, 69.623823],
    radius=50,
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
).add_to(Map)

Map.save('index.html')
webbrowser.open("index.html")
