import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:

    address =input("Enter location: ")

    if len(address) < 1 : break
    apikey=42
    url = serviceurl + urllib.parse.urlencode({'key':apikey,'address':address})

    print('Retrieving',url)
    uh =urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    placeid = js["results"][0]['place_id']
    print("Place id",placeid)
