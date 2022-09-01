import requests
import json
from bs4 import BeautifulSoup
import html_to_json

username = 'vgtgayan'
base_url = 'https://www.kaggle.com/'
url = base_url+str(username)

r = requests.get(url)
print(r.status_code)

html_string = r.text
output_json = html_to_json.convert(html_string)
print(output_json)