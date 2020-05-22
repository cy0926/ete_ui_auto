from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver_path = r'D:\driver\chromedriver.exe'  # 这是chrome驱动路径
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
    #                            'like Gecko) Chrome/81.0.4044.138 Safari/537.36"')
    # driver = webdriver.Chrome(executable_path=driver_path,
    #                           chrome_options=chromeOptions)
    # print(driver.page_source)
    # # 获取请求头信息
    # agent = driver.execute_script("return navigator.userAgent")
    # print(agent)  # 查看请求头是否更改。
    return driver
