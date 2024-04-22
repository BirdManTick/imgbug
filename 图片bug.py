from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 使用Selenium打开网页
n = 1
def a(searchfor,page):
    global n,n1
    driver = webdriver.Chrome()
    driver.get("https://www.hippopx.com/zh/search?q="+str(searchfor)+"&page="+str(page))

    # 等待页面加载
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')))

    # 执行JavaScript代码，将页面滚动到底部，确保所有图片加载出来
    script = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(script)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')))

    # 找到所有目标li元素
    target_li_elements = driver.find_elements(By.CSS_SELECTOR, 'li[itemprop="associatedMedia"]')

    # 遍历所有目标li元素，找到其中的img元素并下载保存到本地
    for index, li in enumerate(target_li_elements, start=1):
        img = li.find_element(By.TAG_NAME, 'img')
        img_src = img.get_attribute('src')
        
        # 下载图片
        img_data = img.screenshot_as_png
        
        # 保存图片到本地
        with open(f'.\\awa\\图片{n}.png', 'wb') as f:
            f.write(img_data)
        n = n + 1
        if n > n1:
            break
    # 关闭浏览器
    driver.quit()

name = input("请输入需要的图片名(类型，如dog,cat)")
n1 = input("请输入需要的图片数")
while True:
    a(name,i)
    i=i+1
    if n > n1:
        break