
from ip_rotator import *
from scrap_proxy import *

if __name__=="__main__":
    updateProxiesList()

    file= open("proxies.txt","r")
    lines=file.readlines()

    ip=lines[0].strip().split()[0]
    port=lines[0].strip().split()[1]

    searchProxySettings()
    turnOnOffSetup()
    changeProxy(ip,port)
    # for line in file:
    #     arr=line.strip().split()
    #     ip=arr[0]
    #     port=arr[1]

    #     print(checkProxyWorking(ip,port))
