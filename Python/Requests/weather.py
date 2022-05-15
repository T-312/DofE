import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.yr.no/en/forecast/daily-table/2-3067696/Czech%20Republic/Hlavn%C3%AD%20m%C4%9Bsto%20Praha/Prague'

with requests.Session() as s:
    response = s.get(url)
    soup = bs(response.text, 'lxml')
    temp = soup.find('div', class_='now-hero__next-hour-temperature-text').text
    rain = soup.find('span', class_='precipitation precipitation--color').text[-3:]
    # wind = soup.find('span', class_='wind__value.observations-card-content__observed-value').text
    print(temp)