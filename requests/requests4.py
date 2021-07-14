import requests

# s = requests.Session() ~ s.close()
# 알아서 열고 닫아줌 ↓

with requests.Session() as s:
    param ={"name":"hong"} # 주소를 따라가는 경우는 param안에

    r=s.get("https://httpbin.org/get", params=param)
    print(r.headers)
    print(r.text)