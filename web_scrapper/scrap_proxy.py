from bs4 import BeautifulSoup
import requests
from config import *


# erasing the previous content of proxies.txt for writing the new set of proxies
with open("proxies.txt","w") as file:
    pass

# getting the html response of the website
html= requests.get(PROXIES_URL)

# getting html code
html_text=html.text

soup=BeautifulSoup(html_text,"lxml")

# accessing the body of the table
table= soup.find("table", class_="table table-striped table-bordered").tbody

# slicing the top 5 latest proxies
top_5= table.find_all("tr")[0: NO_OF_PROXIES :1]

for el in top_5:
    
    ip=el.find_all("td")[0].text            # scraping ip
    port=el.find_all("td")[1].text          # scraping port

    with open("proxies.txt","a") as file:
        file.write(f"{ip} \t")
        file.write(f"{port} \n")





    

    



