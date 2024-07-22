import requests
import json
import time

# 高德地址编码web-API
def get_urls(add):
    url = "https://restapi.amap.com/v3/geocode/geo?address=" + str(add)
    url = url + "&output=json&key=64b6ef3afac2ec44af6a93b50***"
    r = requests.get(url)
    res = json.loads(r.text)
    # 数据格式化;
    content = str(add) + "," + str(res['geocodes'][0]['location']) + "\n"
    print(content)
    print(str(res['geocodes'][0]['location']) + "\n")
    #  写入文件
    # with open(r'data.csv', 'a') as d:
    #     d.write(content)
    # return ""

if __name__ == '__main__':
    get_urls("天府广场")
    
