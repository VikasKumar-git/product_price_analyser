import pyautogui
import time



def searchProxySettings():

    pyautogui.moveTo(430, 1050, duration=0.5)    # going to search box
    pyautogui.click()  

    time.sleep(0.5)

    pyautogui.write("proxy", interval=0.3)   # searching for proxy in settings

    time.sleep(0.5)

    pyautogui.press('enter')  
    time.sleep(0.5)


def turnOnSetup():
    pyautogui.moveTo(1700, 520, duration=0.5)   # going to setup

    pyautogui.click()  

    pyautogui.moveTo(690, 325, duration=0.5)  # coordinates for on/off
    pyautogui.click()

    pyautogui.moveTo(800, 750, duration=0.5)  # coordinates for save
    pyautogui.click()


def changeProxy(ip_address, port):

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


searchProxySettings()

ip_address="54.67.125.45"
port="3128"
turnOnSetup()
changeProxy(ip_address,port)


#--------------------------------------------------------------------------------------------------------

# turing the proxy off

# pyautogui.moveTo(1700, 520, duration=0.5)   # going to setup
# pyautogui.click()  

# pyautogui.moveTo(690, 325, duration=0.5)  # coordinates for on/off
# pyautogui.click()  

# pyautogui.moveTo(800, 750, duration=0.5)  # coordinates for save
# pyautogui.click() 





#--------------------------------------------------------------------------------------------------------
# extra commands


# pyautogui.press('tab')    


# pyautogui.hotkey('ctrl', 's')  

# pyautogui.write(['h', 'e', 'l', 'l', 'o', 'space', 'w', 'o', 'r', 'l', 'd'], interval=0.1)
