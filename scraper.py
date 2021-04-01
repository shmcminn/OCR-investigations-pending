import requests

resp = requests.get('https://www2.ed.gov/about/offices/list/ocr/docs/investigations/open-investigations/tix.html?perPage=1000&sorts%5Binstitution-type%5D=-1')

with open("output.html", 'w') as ofile:
	ofile.write(resp.text)
