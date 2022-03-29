from cgitb import html
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup

def get_token():
    url = 'https://www.era.pt/comprar'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    found = soup.find('input', attrs={'name': '__RequestVerificationToken'})
    return found['value']

payload = {
    "businessTypeId": [],
    "propertiesTypeId": [],
    "locationId": [],
    "shape": "null",
    "bounds": "null",
    "floor": [],
    "eraBenefits": [],
    "otherFeatures": [],
    "propertyState": [],
    "validatePropertyReference": "null",
    "sellPrice": "null",
    "rentPrice": "null",
    "subleasePrice": "null",
    "netArea": "null",
    "landArea": "null",
    "rooms": "null",
    "wcs": "null",
    "parking": "null",
    "onlyDevelopments": "false",
    "page": "1",
    "order": "3"
}

headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["Content-Length"] = "356"
headers["Content-Type"] = 'application/json'
headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
headers["Accept"] = '*/*'
headers["Accept-Language"] = 'en-GB,en;q=0.9,en-US;q=0.8'
headers["Accept-Encoding"] = 'gzip, deflate, br'
headers["RequestVerificationToken"] = get_token()

response = requests.post('https://www.era.pt/API/ServicesModule/Property/Search', headers=headers, data=payload)

print(response, response.headers, response.content)
