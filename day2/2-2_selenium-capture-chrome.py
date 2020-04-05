from selenium import webdriver

driver = webdriver.Chrome('C:\\programs\\webdriver\\chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://www.naver.com/')
driver.implicitly_wait(2)
driver.get_screenshot_as_file('naver_main.png')
driver.quit()

