import sys
from io import BytesIO

import requests
from PIL import Image

from GeocoderParams import get_coordinates, address_to_geocode

address = input()

lon, lat = get_coordinates(address)

geocode = address_to_geocode(','.join([str(lon), str(lat)]))
print(geocode['name'])