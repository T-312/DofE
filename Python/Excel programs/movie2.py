import requests, xlsxwriter, os
from bs4 import BeautifulSoup as bs

url = "https://www.listchallenges.com/completely-random-movie-list"
os.chdir('/Users/tim10')

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
           'upgrade-insecure-requests' : '1',
           'dnt' : '1'}

wb = xlsxwriter.Workbook('Films.xlsx')
ws = wb.add_worksheet()

title = wb.add_format({'bg_color' : 'yellow', 'bold' : True})
ws.set_column(0, 0, 76)

ws.write(0, 0, 'Name', title)
row, col = 1, 0

with requests.Session() as s:
    for i in range(1, 10):
        if i == 1:
            response = s.get(url, headers=headers)

        else:
            response = s.get(url+f'/list/{i}', headers=headers)

        soup = bs(response.text, 'lxml')
        films = soup.find_all('div', class_='item-name')
        films = [' '.join(film.text.split()) for film in films]
        for film in films:
            ws.write(row, col, film)
            row+=1

wb.close()
os.startfile('Films.xlsx')