import requests
import time
import re
from pythonping import ping


username="Your Account"
nettype="njxy"
password="Your Password"



def getIP():
    url = "http://10.10.244.11/"
    res = requests.get(url = url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip



IP_ADDR="www.baidu.com"

while True:
    try:
        message = ping(IP_ADDR)
        if "timed out" in str(message):
            ip=getIP()
            url=f"https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C{username}%40{nettype}&user_password={password}&wlan_user_ip={ip}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=5960&lang=zh"
            response=requests.get(url = url)
    except:
        pass
    time.sleep(5)
