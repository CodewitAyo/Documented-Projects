import requests
from bs4 import BeautifulSoup


def get_product_price(url):
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('span', class_='price-standard')
    if price_element is None:
       price = price_element.text.strip()
       return price
    else:
         return "Price not found."
try: 
    response = requests.get('https://www.birkenstock.com/us/boston-soft-footbed-suede-leather/'
    'boston-suede-suedeleather-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed'
    '-eva-u__46_width=N&dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_size=280&region=US')
    print(get_product_price(response))
except requests.exceptions.RequestException as e:
    print("An error has occured!")


product_url = "https://www.birkenstock.com/us/boston-soft-footbed-suede-leather/boston-suede-suedeleather" \
"-softfootbed-eva-u_46.html?dwvar_boston-suede-suedeleather-softfootbed-eva-u__46_width=N&dwvar_boston-suede" \
"-suedeleather-softfootbed-eva-u__46_size=280&region=US"
price = get_product_price(product_url)
print(f"Product price: {price}")