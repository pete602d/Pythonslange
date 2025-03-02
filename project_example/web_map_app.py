'''
to run this server. 
open codespace
click termonal
type cd project_example/ toi change to the esampel folder
type pip install flask folium requests to install the flask web module the folium map and json requests
type  python web_map_app.py to start the app
'''

from flask import Flask, render_template_string
import folium
import requests

app = Flask(__name__)


# Function to create a Folium map
def create_map():
    map_center = [55.65173979211503, 12.13713929159094]  # Centered at RUC, Denmark
    m = folium.Map(location=map_center, zoom_start=15)

    # URL of the GeoJSON file (raw file from GitHub)
    geojson_url = "https://raw.githubusercontent.com/Esbern/Python-for-Planners/main/data/test.geojson"

    try:
        response = requests.get(geojson_url)
        if response.status_code == 200:
            folium.GeoJson(response.json()).add_to(m)
        else:
            print("Error loading GeoJSON:", response.status_code)
    except Exception as e:
        print("Exception:", e)

    return m._repr_html_()  # Returns the map as an HTML string

@app.route('/')
def home():

    folium_map = create_map()

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask + Folium</title>
    </head>
    <body>

        <h1>Map with GeoJSON Data</h1>
        {folium_map}
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
