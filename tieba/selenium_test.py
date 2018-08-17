"""
本案例用来测试selenium 浏览器爬虫框架
参考文献: https://zhuanlan.zhihu.com/p/27115580
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def selenium_test():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.baidu.com")
    driver.implicitly_wait(3)
    text = driver.find_element_by_id('kw')
    print(text)

    text.clear()

    text.send_keys('python')
    print(driver.title)

    button = driver.find_element_by_id('su')

    button.submit()

    results = driver.find_elements_by_class_name('t')

    for result in results:
        print('标题：{} 超链接：{}'.format(result.text, result.find_element_by_tag_name('a').get_attribute('href')))



    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()

selenium_test()