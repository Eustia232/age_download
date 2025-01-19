from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup




def get_usl_download_url(url):
    # 配置 Edge 浏览器选项
    options = Options()
    options.use_chromium = True
    options.add_argument('--headless')  # 启用无头模式
    options.add_argument('--disable-gpu')  # 禁用 GPU

    # 启动 Edge 浏览器
    driver = webdriver.Edge(options=options)

    # 打开网页
    driver.get(url)

    # 等待页面加载完成，例如等待某个元素加载出来（可以根据你网页的结构更改元素）
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "art-video"))  # 根据实际页面元素修改
    )

    # 获取页面 HTML
    html = driver.page_source

    # 关闭浏览器
    driver.quit()

    soup=BeautifulSoup(html,'html.parser')

    video=soup.select("video.art-video")
    return video[0]['src']


if __name__=='__main__':
    url = 'https://43.240.156.118:8443/vip/?url=age_589fBL9yaXLCuLXTXYh%2BNl5na1cRkdzNmREFWPFl8mt9Mr4Z1jtW5k%2BDKkelo7RBPskKjAPEkFK472YMkucTQTLm%2BA'

    v=get_usl_download_url(url)
    print(v)
