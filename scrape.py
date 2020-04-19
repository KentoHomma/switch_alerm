import requests
from bs4 import BeautifulSoup
import re

# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
content = r'hellow python, 123, end.' 
pattern = 'hel'

result = re.match(pattern, content)


# URLからHTMLを取得します
url  = "https://store.nintendo.co.jp/item/HAD_S_KAYAA.html"
url2 = "https://store.nintendo.co.jp/item/HAD_S_KAYAA.html?c_param=c8739695bc15f0f51b80ceb31f5bddd2"

url_list = [url, url2]

for x in url_list:
    response = requests.get(x)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, 'html.parser')
    
    bs_2 = bs.select_one("body > div.blur_area > div.customize_price\003 \0036\0030_price_info > div > div.customize_price__priceInner > div > p.stock")
    #bs_3 = bs_2「0].select("div", class_="customize_price__inner")
    print("-----------------------------------------------------------------------------------------")
    print("bs_2", bs_2)