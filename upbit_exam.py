# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:36:52 2023

@author: ktaeh
"""

import requests
import json

url="https://api.upbit.com/v1/candles/days"
querystring={"market":"KRW-BTC", "count":"20"}
response = requests.request("GET", url, params=querystring)
print(response.text)
json_response = json.loads(response.text)
#for json in json