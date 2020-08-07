import urllib
import xml.etree.ElementTree as ET
import urllib.request as ur
address = ur.urlopen(" http://py4e-data.dr-chuck.net/comments_871466.xml")
data = address.read()
print(data)

print ('Retrieving', address)

print ('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

count = 0
total = 0
counts = tree.findall('comments/comment')

for i in counts:
    x = i.find('count').text
    total += int(x)
    count += 1
print ('Count:', count)
print ('Sum:', total)
