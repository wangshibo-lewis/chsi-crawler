from flask import Flask, render_template, request, jsonify
from selenium import webdriver
import undetected_chromedriver as uc
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    chsi_code = request.form['chsi_code']
    url2 = f'https://www.chsi.com.cn/xlcx/bg.do?vcode={chsi_code}'
    
    cho = webdriver.ChromeOptions()
    cho.add_argument('--disable-gpu')
    driver = uc.Chrome(headless=True, options=cho, browser_executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    school_info_dict = {}
    try:
        driver.get(url2)
        time.sleep(random.randint(2, 4))

        user_name = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[2]/div[2]')
        user_gender = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[3]/div[2]')
        school_name = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[7]/div[2]')
        school_system = driver.find_element('xpath', '//*[@id="resultTable"]/div/div[2]/div[15]/div[2]')
        
        school_info_dict['user_name'] = user_name.text
        school_info_dict['user_gender'] = user_gender.text
        school_info_dict['school_name'] = school_name.text
        school_info_dict['school_system'] = school_system.text
        
        return jsonify(school_info_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        driver.close()

if __name__ == '__main__':
    app.run(debug=True)