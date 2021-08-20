import requests
import xml.etree.ElementTree as ET

url = 'https://api.geekdo.com/xmlapi2/thing?thing=boardgame&id=1198'

xml = ET.fromstring(requests.get(url).content)[0]
image = xml.find('image').text
thumbnail = xml.find('thumbnail').text
description = xml.find('description').text
name = xml.find('name').attrib['value']
publisher = xml.find('link[@type="boardgamepublisher"]').attrib['value']
year = xml.find('yearpublished').attrib['value']

print(image)
print(description)
print(name)
print(publisher)
print(year)
