import requests
from bs4 import BeautifulSoup

page = requests.get("https://version3.guestworkervisas.com/newversionemailer.php")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())