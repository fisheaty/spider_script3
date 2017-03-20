import csv
from download import download_agent as D
import json

writer = csv.writer(open('countries.csv', 'w'))

html = D('http://example.webscraping.com/ajax/search.json?page=0&page_size=1000&search_term=.')
ajax = json.loads(html)
for record in ajax['records']:
	row = [record['country']]
	writer.writerow(row)