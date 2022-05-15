from flask import *
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.yr.no/en/forecast/daily-table/2-3067696/Czech%20Republic/Hlavn%C3%AD%20m%C4%9Bsto%20Praha/Prague'

with requests.Session() as s:
    response = s.get(url)
    soup = bs(response.text, 'lxml')
    temp = ''.join([soup.find('div', class_='now-hero__next-hour-temperature-text').text, 'C'])
    rain = soup.find('span', class_='precipitation precipitation--color').text[-3:]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", current_temp=temp)

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()