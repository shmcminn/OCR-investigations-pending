print('importing')
import json

import requests
from bs4 import BeautifulSoup
print('finished importing')

resp = requests.get('https://www2.ed.gov/about/offices/list/ocr/docs/investigations/open-investigations/tix.html?perPage=1000&sorts%5Binstitution-type%5D=-1')

print("made request")

soup = BeautifulSoup(resp.text, 'html.parser')

table = soup.select("#oi-table")[0]

header_thtags = table.select('thead  tr  th')

export_data = []

headers = []

for thtag in header_thtags:
	headers.append(thtag.get_text())

rows = table.select('tr')

for row in rows:
	d = {} 
	for ind, td in enumerate(row.select('td')):
		d[headers[ind]] = td.get_text()
	if len(d) > 0:
		export_data.append(d)

with open("output.html", 'w') as ofile:
	ofile.write(resp.text)
ofile.close()

with open("output.json", 'w') as ofile:
	ofile.write(json.dumps(export_data))
ofile.close()

