import undetected_chromedriver as uc
from selenium import webdriver
from pyvirtualdisplay import Display
import requests

import re
import time
import random
 
display = Display(visible=0, size=(2560, 1440), color_depth=16)
display.start()

cho = webdriver.ChromeOptions()
cho.add_argument('--disable-gpu')  # 禁用GPU加速
driver = uc.Chrome(headless=False, options=cho, browser_executable_path='/opt/google/chrome/google-chrome')

url = 'https://www.chsi.com.cn'
url1 = 'https://www.chsi.com.cn/xlcx/bgcx.jsp'
url2 = 'https://www.chsi.com.cn/xlcx/bg.do?vcode=ASLMN1RQZPRMHX05'

driver.get(url2)
time.sleep(3)
driver.save_screenshot('nowsecure.png')

cookies = driver.get_cookies()
cache_cookie = {}
for cookie in cookies:
	cache_cookie[cookie['name']] = cookie['value']

print(cache_cookie)



session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
})

cookies = {
    'JSESSIONID': '645D64B97FC59C88CED207242E1C82DD',
    'CHSICC_CLIENTFLAGCHSI': '49c3174718c3b560a1040e55b347631e',
    '_ga': 'GA1.3.253536503.1736285654',
    '_ga_8YMQD1TE48': 'GS1.1.1736285653.1.0.1736285653.0.0.0',
    'aliyungf_tc': '28b349d43fdd6265cf878800464bfc4b3d34cd2d2cb50047d0d236ddbb305b9c',
	'CHSICC01': '!HveurY8ZP6ZrpG4nVPBkiJOoJxwY2sBB+9chAe38AGVrn2SH4voRzhFdKtgbO9Qc7pc/xDHLZy5Sqg==',
    'acw_tc': 'ac11000117362856521522376ee9de2589320e12500253f9800589d6c6b80d',
	'goaYXsyEWlxdP': cache_cookie['goaYXsyEWlxdP'],
    'goaYXsyEWlxdO': cache_cookie['goaYXsyEWlxdO'],
}
session.cookies.update(cookies)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',  # 注意：requests 库会自动处理压缩编码
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.chsi.com.cn/xlcx/bgcx.jsp',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

response = session.get(url2, headers=headers)

if response.status_code == 200:
    print("success: 200")
    print(response.text)
else:
    print(f"fali: {response.status_code}")
    print(response.text)




driver.close()

display.stop()



