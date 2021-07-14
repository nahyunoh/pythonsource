#python.org

import requests


with requests.Session() as s:
    r=s.get("https://www.python.org/")
    print(r.text)