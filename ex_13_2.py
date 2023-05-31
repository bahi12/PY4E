import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1807949.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

json_data = json.loads(data)
comments = json_data['comments']

total = 0
total_co = 0


for comment in comments:
    count = comment['count']
    total += count
    total_co += 1
print('Count', total_co)
print(total)
