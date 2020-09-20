from selenium import webdriver


def get_driver():
    # driver = webdriver.Chrome() # 默认是有界面

    # 无头浏览器运行设置
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--start-maximized")
    option.add_argument("--no-sandbox")
    option.add_argument("--headless")  # 浏览器不提供可视化页面
    option.add_argument('--log-level=3')
    driver = webdriver.Chrome(chrome_options=option)

    return driver
