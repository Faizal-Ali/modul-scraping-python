from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

rsc_url = "https://www.kompas.com/ramadhan/jadwal-imsakiyah/kota-surabaya"

rsc = urlopen(rsc_url).read()
soup = bs(rsc, 'html.parser')
buka_puasa = soup.find("tr", {"class": "jadwalrmdCurrent"})
judul = soup.find_all("th")

for a in range(0,len(judul)):
    print(judul[a].text+" => "+buka_puasa.select('td')[a].text)