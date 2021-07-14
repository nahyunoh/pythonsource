import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/"

response=requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')

# gmarket 전체 카테고리 출력
# category=soup.find_all("span",class_="link__1depth-item")
# print("전체 카테고리:{}".format(category))

ul=soup.find("ul", class_="list__category-all")

# 1차 카테고리
# category_list=ul.find_all("span", class_="link__1depth-item") # list 형태로 들어옴
# #print(category_list)

# # list 형태 => for문 이용
# for category in category_list:
#     print(category.string)


# 2차 카테고리

# div=soup.find("div",class_="box__category-2depth")
# print(div)
# category2=div.find_all("a", class_="link__2depth-item")
# print(category2)

# for category in category_list_2depth:
#     print(category.string)        => 첫번째 꺼만 가져옴


category_list_2depth = ul.find_all("li", class_="list-item__2depth")
# print(category_list_2depth)

for item in category_list_2depth:
    print(item.string)
