import requests
from bs4 import BeautifulSoup

page = requests.get("https://version3.guestworkervisas.com/newversionemailer.php")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all(id="example")
rows = table[0].select("tbody tr")


for row in rows:
    mail = row.select("td")[2].get_text()
    recruiter_title = row.select("td")[5].get_text()
    print(mail, "||", recruiter_title)
    print(type(mail), type(recruiter_title))
