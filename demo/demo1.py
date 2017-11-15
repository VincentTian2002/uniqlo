import time, os
from selenium import webdriver
import robot

class UniqloDemo(object):

    def __init__(self):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        driver_server = os.path.join(dir_path, 'lib/IEDriverServer.exe')
        os.environ['webdriver.ie.server'] = 'driver_server'
        self.driver = webdriver.Ie(driver_server)
        self.driver.maximize_window()

    def open_uniqlo(self, url):
        self.driver.get(url)
        # self.driver.implicitly_wait(15)

    def close_brwoser(self):
        self.driver.quit()

    def navigate_to_cart(self, locator):
        # time.sleep(10)
        print self.driver.title
        print self.driver.window_handles
        element = self.driver.find_element_by_xpath(locator)
        # oaction = webdriver.ActionChains(self.driver)
        # oaction.click(element).perform()
        # oaction.move_to_element(element).perform()
        # time.sleep(3)
        # oaction.double_click(element).perform()
        time.sleep(3)
        element.click()
        # element.send_keys('python')
        # self.driver.find_element_by_id('su').click()


if __name__ == '__main__':
    demo = UniqloDemo()
    demo.open_uniqlo('http://www.uniqlo.com/jp/')
    # demo.open_uniqlo('http://www.baidu.com')
    cart_locator = '//div[@id="gnav_util_area"]/ul[2]/li[4]/a[1]'
    # cart_locator = '//img[@src="https://im.uniqlo.com/images/jp/pc/img/material/nav/btn_nav_utility05_JP.gif"]'
    # cart_locator = 'tj_trhao123'
    demo.navigate_to_cart(cart_locator)
    print 'navigated to cart subflow.'
    time.sleep(3)
    demo.close_brwoser()
    print 'Done!'


