# 1.需要能翻墙
# 2.需要提前将浏览器对应版本的selenium驱动放到python解释器同一目录下
import pandas as pd
from selenium.webdriver.common.by import By

# 在pd.read_excel(填入本地文献Excel)
wx = pd.read_excel('C:\\Users\XMICUser\Desktop\文献列表.xls')
wx_list = []
for i in range(wx.__len__()):
    dd = str(wx.iloc[i, 0])
    wx_list.append(dd.strip())

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://scholar.google.com/")
output = []

def cite_or_bib(cite=True):
    for ee in wx_list:
        # 输入文献名
        inputElement = driver.find_element(value="gs_hdr_tsi")
        inputElement.clear()
        inputElement.send_keys(ee)

        # 点击搜索按钮
        driver.find_element(value="gs_hdr_tsb").click()
        time.sleep(2)

        # 点击引用按钮
        driver.find_element(by=By.CLASS_NAME, value='gs_or_cit.gs_nph').click()
        time.sleep(2)

        # 如果需要输出引用文件
        if cite == True:
            # cite
            # 选择GB/T
            yy = driver.find_element(by=By.CLASS_NAME, value='gs_citr').text
            with open('yy.txt', 'a') as f:
                f.write(yy)
                f.write('\n')
            driver.back()
            driver.back()

        # 如果需要输出bib文件
        else:
            # bib
            driver.find_element(by=By.CLASS_NAME, value='gs_citi').click()
            bib = driver.find_element(by=By.XPATH, value="//*").text
            with open('bib.txt', 'a') as f:
                f.write(bib)
                f.write('\n')
            driver.back()
            driver.back()
            driver.back()

if __name__ == '__main__':
    cite_or_bib(True)
