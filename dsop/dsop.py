import requests
import json

# POST请求的URL
url = "https://tsm.cmpay.com/tsmui_new_pro/html/query/index/tsmCoreSync/se_detail.CoreSeApplication_se/"
#https://tsm.cmpay.com/tsmui_new_pro/html/query/index/tsmCoreSync/se_detail.CoreSeApplication_se/
# 要发送的数据，通常是一个字典（dict）
data = {
    'se': '150000000041938922',
    'serverInfoCode': 'xiqu',
    'status': 'UNDOWNLOAD',
    '_pageSize': '10',
    '_pageNo': '1',
    '_orderBy': '',
    'totalCount': '10',
    'totalPage': '10',
    'pageNo': '1'


}

# 将字典转换为JSON格式的字符串
json_data = json.dumps(data)
""" 
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 92
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: route=ef0af51fa840b8ed0ae311ff2c8cf995; JSESSIONID=F868FC549979DE0B2CD31BC771C0DF37
Host: tsm.cmpay.com
Origin: https://tsm.cmpay.com
Referer: https://tsm.cmpay.com/tsmui_new_pro/ent/se/seManager.html
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301
X-Requested-With: XMLHttpRequest
"""
# 自定义的头部信息
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',  # 指定内容类型为JSON
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301',  # 示例：添加了一个Bearer令牌
    'Cookie': 'route=ef0af51fa840b8ed0ae311ff2c8cf995; JSESSIONID=2257B078D92A85D869E516BBD62FB209',
    # 'User-Agent': 'my-app/0.0.1',  # 可以添加自定义User-Agent
    # 添加其他需要的头部信息
}

# 发送POST请求，包含头部信息
sendData='se=150000000047383752&serverInfoCode=xiqu&status=UNDOWNLOAD&_pageSize=10&_pageNo=1&_orderBy='
response = requests.post(url, data=sendData, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    print("请求成功。")
    # 获取响应内容
    response_content = response.content
    print(response_content)
else:
    print("请求失败，状态码：", response.status_code)

# 你还可以获取JSON格式的响应内容
response_json = response.json()
print(response_json)