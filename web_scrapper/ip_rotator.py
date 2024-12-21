import pyautogui
import time
from config import *
from bs4 import BeautifulSoup
import requests
import subprocess

def searchProxySettings():
    """this function searches for proxy settings in the windows search"""

    pyautogui.moveTo(470, 1050, duration=0.5)    # going to search box
    pyautogui.click()  

    time.sleep(0.5)

    pyautogui.write("proxy", interval=0.3)   # searching for proxy in settings

    time.sleep(0.5)

    pyautogui.press('enter')  
    time.sleep(0.5)


def turnOnOffSetup():
    """this function turns on the setup option in the proxy settings"""

    pyautogui.moveTo(1700, 520, duration=0.5)   # going to setup

    pyautogui.click()  

    pyautogui.moveTo(690, 325, duration=0.5)  # coordinates for on/off
    pyautogui.click()

    pyautogui.moveTo(800, 750, duration=0.5)  # coordinates for save
    pyautogui.click()


def changeProxy(ip_address, port):
    """ this function takes in ip address and port and changes 
    the present ip address and port in the settings
    """

    pyautogui.moveTo(1700, 520, duration=0.5)   # going to setup

    pyautogui.click()  

    # pyautogui.moveTo(690, 325, duration=0.5)  # coordinates for on/off
    # pyautogui.click()  

    # time.sleep(0.5)

    pyautogui.moveTo(740, 440, duration=0.5)  # coordinates for writing the ip
    pyautogui.click() 

    pyautogui.moveTo(860, 440, duration=0.5)  # cancelling the previous ip
    pyautogui.click() 


    pyautogui.write(ip_address, interval=0.2)   # writing ip

    pyautogui.moveTo(930, 440, duration=0.5)  # coordinates for writing the port

    for i in range(0,3):
        pyautogui.click() 

    pyautogui.write(port, interval=0.2)   # writing port


    pyautogui.moveTo(800, 750, duration=0.5)  # coordinates for save
    pyautogui.click() 



def checkProxyWorking(ip_address,port):
    """this function takes input and checks if the ip is working or not"""
        
    result = subprocess.run(
    ["ping", "-n", "1", ip_address], 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )
    if result.returncode==0:
        return True
    else:
        return False
    
def updateProxiesList():
    """
    this function scrapes the latest ip addresses and ports and 
    updates them to the proxies.txt
    """

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
    

def main():
    searchProxySettings()

    updateProxiesList()


    while(True):
        updateProxiesList()
        turnOnOffSetup()

        file=open("proxies.txt","r")

        for line in file:
            
            arr=line.strip().split()
            ip=arr[0]
            port=arr[1]

            while(checkProxyWorking(ip,port)):
                changeProxy(ip,port)
                time.sleep(5)
        
        turnOnOffSetup()

            



if __name__=="__main__":
    main()





#--------------------------------------------------------------------------------------------------------

# turing the proxy off

# pyautogui.moveTo(1700, 520, duration=0.5)   # going to setup
# pyautogui.click()  

# pyautogui.moveTo(690, 325, duration=0.5)  # coordinates for on/off
# pyautogui.click()  

# pyautogui.moveTo(800, 750, duration=0.5)  # coordinates for save
# pyautogui.click() 





