from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.marksandspencer.com/l/gifts/gifts-for-her#intid=Christmas_LP_hero-mosaic_121023_gifts_for_her').text
soup = BeautifulSoup(html_text, 'lxml')
name = soup.find('div', class_='css-1p0u01m e3yws130')
company = name.find('span', class_ = "css-uaryup e1mond8w9").text.replace(' ', '')
print(company)
price = name.find('span', class_ = "css-8hxi51 e12i2by41").text.replace(' ', '')
print(price)