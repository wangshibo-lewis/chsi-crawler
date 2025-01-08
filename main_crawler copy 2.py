import undetected_chromedriver as uc
from selenium import webdriver

import re
import time
import random
from requests.cookies import RequestsCookieJar
 

url = 'https://www.chsi.com.cn/xlcx/bg.do?vcode=ASLMN1RQZPRMHX05'

options = webdriver.ChromeOptions()
# options.add_argument('--disable-gpu')  # 禁用GPU加速
# options.add_argument('--no-sandbox')  # 禁用沙盒模式
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
# options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化控制特征
# options.add_argument("--window-size=1920x1080")  # 设置窗口大小
driver = uc.Chrome(headless=False, browser_executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', options=options)

driver.get(url)
time.sleep(3)

cookies = driver.get_cookies()
jar = RequestsCookieJar()
# goaYXsyEWlxdP = ''
cache_cookie = {}
for cookie in cookies:
	# if cookie['name'] == 'goaYXsyEWlxdP':
		# print(cookie['value'])
		# goaYXsyEWlxdP = cookie['value']
	cache_cookie[cookie['name']] = cookie['value']
    # jar.set(cookie['name'], cookie['value'])

# print(goaYXsyEWlxdP)
print(cache_cookie)

# 打开指定的URL

# for i in range(1, 10):
# 	driver.get(url)
# 	time.sleep(random.randint(1, 3))
# 	school_system = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[15]/div[2]')
# 	print(school_system.text)
# 	driver.save_screenshot('nowsecure{}.png'.format(i))
# 	time.sleep(random.randint(1, 5))

import requests

# 创建一个会话对象
session = requests.Session()

# 设置 User-Agent
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
})

# 添加 cookies
cookies = {
    'JSESSIONID': '645D64B97FC59C88CED207242E1C82DD',
    'CHSICC_CLIENTFLAGCHSI': '49c3174718c3b560a1040e55b347631e',
    '_ga': 'GA1.3.253536503.1736285654',
    '_ga_8YMQD1TE48': 'GS1.1.1736285653.1.0.1736285653.0.0.0',
    'aliyungf_tc': '28b349d43fdd6265cf878800464bfc4b3d34cd2d2cb50047d0d236ddbb305b9c',
	'CHSICC01': '!HveurY8ZP6ZrpG4nVPBkiJOoJxwY2sBB+9chAe38AGVrn2SH4voRzhFdKtgbO9Qc7pc/xDHLZy5Sqg==',
    'acw_tc': 'ac11000117362856521522376ee9de2589320e12500253f9800589d6c6b80d',
    # 'goaYXsyEWlxdO': '60noV7xexWFIAtjR5Xwn9dij9G1Mhd04vxI1KZxxBb9grIhR0HxSzthCTW_Y1htLrqzHeUMuPdgpjrPE6oyBXAja',
	# 'goaYXsyEWlxdP': goaYXsyEWlxdP,
     
    # 'aliyungf_tc': cache_cookie['aliyungf_tc'],
	# 'CHSICC01': cache_cookie['CHSICC01'],
    # 'acw_tc': cache_cookie['acw_tc'],
	'goaYXsyEWlxdP': cache_cookie['goaYXsyEWlxdP'],
    'goaYXsyEWlxdO': cache_cookie['goaYXsyEWlxdO'],

}


# {'_gid': 'GA1.3.354448534.1736285654', 
#  '_ga_8YMQD1TE48': 'GS1.1.1736285653.1.0.1736285653.0.0.0', 
#  '_ga': 'GA1.3.253536503.1736285654', 
#  'HMACCOUNT': '6307D9CF4B2D9B9A', 
#  'Hm_lvt_9c8767bf2ffaff9d16e0e409bd28017b': '1736285654', 
#  '_gat_gtag_UA_100524_1': '1', 
#  'CHSICC01': '!HveurY8ZP6ZrpG4nVPBkiJOoJxwY2sBB+9chAe38AGVrn2SH4voRzhFdKtgbO9Qc7pc/xDHLZy5Sqg==', 
#  'goaYXsyEWlxdP': '0usZ33MJRe81LfFbzKrb5fyFCxHoMwhRWaOWdabL5MbS7dx4Zfgy48A3XQMbtJeUaKVeSpGtOSJhP1qWivYbME6.aVJ0pCvAwSzr9_4kV2mt0c5O7XY2RMI5BUWdnauAIIR34w_EZpTMW5i1BQa4JJExqlz_K7B9tsKfnwi10mVmqaQw.Pm7AUoW5jgXGmDXYqCUQ53Eq6hfyHe1ewkUJr9A.er9KzFHIs71nHkaObKePYSYybBEKrrFdh90fsyPMWKQZaTP2BM0z9lugPZmgrHU6JxlnK7RcyZ6E51ISiG0', 
#  'acw_tc': 'ac11000117362856521522376ee9de2589320e12500253f9800589d6c6b80d', 
#  'CHSICC_CLIENTFLAGCHSI': '49c3174718c3b560a1040e55b347631e', 
#  'Hm_lpvt_9c8767bf2ffaff9d16e0e409bd28017b': '1736285654', 
#  'aliyungf_tc': '28b349d43fdd6265cf878800464bfc4b3d34cd2d2cb50047d0d236ddbb305b9c', 
#  'JSESSIONID': '645D64B97FC59C88CED207242E1C82DD', 
#  'goaYXsyEWlxdO': '604rDkBw9PUcsv1RoTv9bReiDzjBT61WDsHLPNqZlcwzFUmX5bNk8ERJRAF_BN2OrwImVFX1LgK3BQe82GnBYJ3A'}
# 更新会话中的 cookies
session.cookies.update(cookies)

# 设置额外的头部信息
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',  # 注意：requests 库会自动处理压缩编码
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    # 'Referer': 'https://www.chsi.com.cn/xlcx/bgcx.jsp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

# 发送 GET 请求
response = session.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    print("请求成功")
    # 打印响应内容（前1000个字符）
    print(response.text)
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)




driver.close()





