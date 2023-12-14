import requests
from bs4 import BeautifulSoup
# スクレイピング対象のURL
url = "https://example.com"
# ページのHTMLを取得
response = requests.get(url)
html = response.text
# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html, "html.parser")
# タイトルを取得
title = soup.title.text
# リンクの一覧を取得
links = soup.find_all("a")
link_urls = [link["href"] for link in links]
# 結果を出力
print("タイトル:", title)
print("リンク一覧:")
for link_url in link_urls:
    print(link_url)
