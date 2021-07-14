import urllib.request as req


# 파일 URL
file_url ="https://postfiles.pstatic.net/20111223_251/selin17_1324584617402OxIsh_JPEG/%B0%AD%BE%C6%C1%F61.jpg?type=w3"

# 다음 메인페이지 URL\
html_url ="https://www.daum.net/"  #urllib.error.URLError

#e 다운로드 받을 경로
save_img="c:/dog.jpg"
save_html="c:/daum.html"

try:
    file1, header1=req.urlretrieve(file_url, save_img)
    file2, header2=req.urlretrieve(html_url, save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("다운로드 성공")