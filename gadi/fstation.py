import urllib.request
from bs4 import BeautifulSoup
def fuel_station():
    wiki = "https://www.google.com/maps/search/petrolbunksnearme/"
    page = urllib.request.urlopen(wiki)
    soup = str(BeautifulSoup(page, features="lxml"))
    path = 'D:\\Gadi_By_FlasK\\Gadi_By_FlasK\\templates\\fuelstation.html'
    k=soup.find('html')
    with open(path, 'w') as f:
        for i in k:
            f.write(i)

fuel_station()