import urllib.request
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1807948.xml'

with urllib.request.urlopen(url, context=ctx) as response:
    xml_data = response.read()

tree = ET.fromstring(xml_data)

counts = tree.findall('.//count')
comments = []
for count in counts:
    comments.append(count.text)
print(sum(int(n) for n in comments))
