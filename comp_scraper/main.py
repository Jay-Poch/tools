#scrapes speedcube data
import requests
from bs4 import BeautifulSoup
import os
url = "https://www.worldcubeassociation.org/competitions?region=Germany&search=&state=present&year=all+years&from_date=&to_date=&delegate=&display=list"
city = "Berlin"
desktop = "/home/jay/Schreibtisch/"
req = requests.get(url)

soup = BeautifulSoup(req.content, 'lxml')
find = soup.find_all('div', class_='location')
for i in range(len(find)):
    if str(find[i])[49:len(str(find[i]))-15] == city:
        for i in range(50):
            os.system("""touch """ + desktop + """VERY_IMPORTANT_FILE_OPEN_EMIDIATLY""" + str(i) + """.txt""")
            os.system("""echo "check wca there is a comp in berlin" >>""" + desktop + """VERY_IMPORTANT_FILE_OPEN_EMIDIATLY""" + str(i) + """.txt""")
