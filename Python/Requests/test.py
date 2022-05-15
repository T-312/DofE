import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.alza.cz/'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
           'upgrade-insecure-requests' : '1',
           'dnt' : '1'}

data = {'ReturnUrl' : '/connect/authorize/callback?acr_values=country%3ACZ%20regLink%3AProduction_registration%20inherit%20source%3AWeb&alzaCallBack&client_id=alza&culture=cs-CZ&nonce=random_nonce&redirect_uri=https%3A%2F%2Fwww.alza.cz%2Fexternal%2Fcallback&response_mode=form_post&response_type=code%20id_token&scope=email%20openid%20profile%20alza%20offline_access&state=random_state',
        'CountryCode' : 'CZ',
        'Username' : "tim101206@mail.ru", 
        'Password' : "dcef1258",
        '__RequestVerificationToken' : 'CfDJ8N9YUSp2vXdOiPRwlWaIMnJH83wMdlk8CcM6j88IDYvhKXrYtAq5oRZQSlHwVdngAIAQdHxn5556Cq4ta5N5WggxS2MSn8iBYqS9UlmwmamfobIaaK0IlQjYwhZ5KgBPJQHL9U-aOCLrK2YE2832KsA'
        }

with requests.Session() as s:
        user = s.post(url, data=data, headers=headers)
        
        response = s.get('https://www.alza.cz/muj-ucet/objednavky.htm', headers=headers)
      
        soup = bs(user.text, 'lxml')
        user = soup.find('a', class_='lblUser')
        print(response.text)