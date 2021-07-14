import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

weather_url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"


text=req.urlopen(weather_url).read().decode("utf-8")


print(text[:1000])