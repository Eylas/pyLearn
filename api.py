import requests
import json
import csv
import urllib
from pprint import pprint

response = requests.get("https://api.spacexdata.com/v3/launches?filter=flight_number,launch_date_utc")
launch = response.json()

print(launch)

with open ('launchDate.json', 'w') as f:
   json.dump(launch,f,ensure_ascii=False, indent=4)    

