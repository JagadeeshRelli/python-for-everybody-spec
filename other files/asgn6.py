import json
import urllib

count = 0
sum = 0
url = input("Enter Url - ")

data = urllib.urlopen(url).read()

print(data)
info = json.loads(str(data))

for i in info['comments']:
    count = count+1
    sum = sum + i['count']
print("Sum : ",sum)  
print("count : ",count)
