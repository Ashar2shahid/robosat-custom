import os
import glob
import re

files = glob.glob('./*.geojson')

for geojsons in files:
    with open(geojsons, 'r+') as f:
        data = f.read()
        data = re.sub(r'"coordinates": \[\s(.*)\]', r'"coordinates": \1', data)
        data = re.sub(r'MultiPolygon', r'Polygon', data)
        f.seek(0)
        f.write(data)
        f.truncate()
