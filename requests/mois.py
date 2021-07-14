import requests

# urlparse3.py 변경

api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params=[]

for num in [1001,1012,1013,1014]:
    params.append(dict(ctxCd=num)) # dict(키=value)

# 확인
# print(params) 

with requests.Session() as s:
    for c in params:

        # 요청
        r=s.get(api,params=param)

        # 출력
        print("-"*100)
        print(data)

