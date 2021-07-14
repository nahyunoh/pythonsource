import urllib.request as req


# 좋아하는 연예인 사진 가져오기

# 파일 URL
file_url ="https://newsimg.sedaily.com/2021/07/02/22OR8RMABZ_3.jpg"
# 다음 메인페이지 URL
html_url ="https://www.daum.net/" 

# 다운받을 경로
save_img="c:/vv.jpg"
save_html="c:/daum.html"

try:
    file1, header1 = req.urlretrieve(url, save_path)
except Exception:
    print("다운로드 실패")
else:
    print(header1)
    print("다운로드 성공")