import requests
from bs4 import BeautifulSoup

URL = 'https://www.binance.com/ru/markets'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r

def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='css-vlibs4')

	btc = []
	for item in items:
		btc.append({
			'title': item.find('div', class_="css-1x8dg53").get_text(),
			'price': item.find('div', class_="css-ydcgk2").get_text(),
			'procent': item.find('div', class_="css-18yakpx").get_text()
			})
	print(f"{btc}\n")

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		get_content(html.text)
	else:
		print('Error')


parse()