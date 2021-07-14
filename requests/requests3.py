import requests

s = requests.Session()

# get 방식
# r = s.get("https://httpbin.org/get")
# print(r.text)

# post 방식 => 폼안에있는 데이터 전송 개념으로 처리
data={
    "name":"hong",
    "id":"hong123"
}
r =s.post("https://httpbin.org/post", data=data)
print(r.text)


# delete 방식
# r = s.delete("https://httpbin.org/delete")
# print(r.text) 

# put 방식(patch) :: post와 비슷
# data={
#     "name":"hong"
# }
# r =s.put("https://httpbin.org/put", data=data)
# print(r.text)

s.close()