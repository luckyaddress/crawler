#-*- coding: utf-8 -*- 
# 使用中文註解，要加上上面那一行的編碼

from urllib.request import urlopen
# 到Python3 之後，用法有改變，要使用urllib.request去使用 urlopen

from bs4 import BeautifulSoup

quote_page = 'https://www.ithome.com.tw/'
page = urlopen(quote_page)
# 開啟指定的頁面用法
content = page.read()
# 讀取該頁面內容
#content_encoding = content.decode('utf8')
# 重新編碼讀取之頁面

soup = BeautifulSoup(content, 'html.parser')

name_box = soup.find_all('div','category_label')
# 使用find會傳回第一筆資料，使用find_all可傳回所有符合條件的資料

print(soup)
# 將抓取到的資料，重新編碼
print(name_box)

