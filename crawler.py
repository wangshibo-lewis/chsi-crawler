import undetected_chromedriver as uc
from selenium import webdriver
# from pyvirtualdisplay import Display
import time
import random
 
# display = Display(visible=0, size=(2560, 1440), color_depth=16)
# display.start()

cho = webdriver.ChromeOptions()
cho.add_argument('--disable-gpu')
driver = uc.Chrome(headless=False, options=cho, browser_executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

chsi_code = input('Input chsi code: ')
url2 = 'https://www.chsi.com.cn/xlcx/bg.do?vcode={}'.format(chsi_code)

driver.get(url2)
time.sleep(random.randint(2, 4))

school_info_dict = {}
try:
    user_name = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[2]/div[2]')
    user_gender = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[3]/div[2]')
    school_name = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[7]/div[2]')
    school_system = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[15]/div[2]')
    school_info_dict['user_name'] = user_name.text
    school_info_dict['user_gender'] = user_gender.text
    school_info_dict['school_name'] = school_name.text
    school_info_dict['school_system'] = school_system.text
    for k, v in school_info_dict.items():
        print(k, v)
except Exception as e:
    print(repr(e))
    print('error happen when getting chsi report: ')

    try:
        chsi_msg = driver.find_element('xpath', '//*[@id="msgDiv"]')
        print('    chis_msg: ', chsi_msg.text)
    except Exception as e:
        print('    crawler dead: ', repr(e))


driver.close()
# display.stop()
