import os
import requests
import urllib
from tqdm import tqdm

"""
카카오톡 이모티콘 샵에서 원하는 이모티콘을 찾은 뒤
https://e.kakao.com/t/(이모티콘 이름)
위와 같은 링크에서 이모티콘 이름 부분을 입력하세요.
"""

ename = input("이모티콘 이름(영문): ")

url = "https://e.kakao.com/api/v1/items/t/" + ename
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
res = requests.get(url, headers=headers)
status = res.status_code

if status == 200:
    res = res.json()
    title = res["result"]["title"]
    images = res["result"]["thumbnailUrls"]

    print("<" + title + "> 이모티콘을 다운로드하는 중...")

    os.makedirs(title, exist_ok=True)
    for i, imageUrl in enumerate(tqdm(images, bar_format="{l_bar}{bar:10}{r_bar}{bar:-10b}"), start=1):
        path = os.path.join(title, str(i) + ".jpg")
        urllib.request.urlretrieve(imageUrl, path)

    print("다운로드가 완료되었습니다.")

elif status == 404:
    raise Exception("존재하지 않는 이모티콘입니다.")
else:
    raise Exception("알 수 없는 예외가 발생했습니다. Status Code: " + status)








