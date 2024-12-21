

from ip_rotator import *

if __name__=="__main__":
    updateProxiesList()


    file=open("proxies.txt","r")

    for line in file:

        arr=line.strip().split()
        ip=arr[0]
        port=arr[1]

        if checkProxyWorking(ip,port):
            print("proxy is working")
        else:
            print("not working")