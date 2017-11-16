import os
import time
from selenium import webdriver
from demo.constant.commonconst import CommonConst
from selenium.webdriver.support.select import Select


class WebDriverFunc(object):
    def __init__(self):
        self._driver = None

    def get_driver(self):
        return self._driver

    def locate_element(self, locator):
        pattern = locator.split('=', 1) if '=' in locator else []
        if not (all(pattern) and pattern):
            raise Exception('please provide locator!')
        key, value = pattern
        if key == 'id':
            element = self._driver.find_element_by_id(value)
        elif key == 'name':
            element = self._driver.find_element_by_name(value)
        elif key == 'xpath':
            element = self._driver.find_element_by_xpath(value)
        else:
            raise Exception('wrong By!')
        return element

    def locate_elements(self, locator):
        pattern = locator.split('=', 1) if '=' in locator else []
        if not (all(pattern) and pattern):
            raise Exception('please provide locator!')
        key, value = pattern
        if key == 'id':
            elements = self._driver.find_elements_by_id(value)
        elif key == 'name':
            elements = self._driver.find_elements_by_name(value)
        elif key == 'xpath':
            elements = self._driver.find_elements_by_xpath(value)
        else:
            raise Exception('wrong By')
        return elements

    @staticmethod
    def locate_element_by_element(web_element, locator):
        pattern = locator.split('=', 1) if '=' in locator else []
        if not (all(pattern) and pattern):
            raise Exception('please provide locator!')
        key, value = pattern
        if key == 'id':
            element = web_element.find_element_by_id(value)
        elif key == 'name':
            element = web_element.find_element_by_name(value)
        elif key == 'xpath':
            element = web_element.find_element_by_xpath(value)
        else:
            raise Exception('wrong By pattern!')
        return element

    def select_from_drop_down_list(self, locator, index=None, value=None, text=None):
        ele = self.locate_element(locator)
        selection = Select(ele)
        if index:
            selection.select_by_index(index)
            return
        if value:
            selection.select_by_value(value)
            return
        if text:
            selection.select_by_visible_text(text)

    @staticmethod
    def locate_elements_by_element(web_element, locator):
        pattern = locator.split('=', 1) if '=' in locator else []
        if not (all(pattern) and pattern):
            raise Exception('please provide locator!')
        key, value = pattern
        if key == 'id':
            elements = web_element.find_elements_by_id(value)
        elif key == 'name':
            elements = web_element.find_elements_by_name(value)
        elif key == 'xpath':
            elements = web_element.find_elements_by_xpath(value)
        else:
            raise Exception('wrong By pattern!')
        return elements

    def wait_util_element_exist(self, locator, timeout=30, poll=0.5):
        while True:
            end_time = time.time() + timeout
            ele = self.locate_element(locator)
            if ele:
                return True
            time.sleep(self.poll)
            if time.time() > end_time:
                return False

    def element_is_exist(self, locator):
        element = self.locate_element(locator)
        return element.is_displayed()

    def element_is_enabled(self, locator):
        element = self.locate_element(locator)
        return element.is_enabled()

    def open_browser(self, browser_type):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        driver_path = os.path.join(os.path.dirname(dir_path), CommonConst.DRIVER_PATH)
        os.environ['driver'] = driver_path
        if browser_type.lower() == 'ie':
            self._driver = webdriver.Ie(driver_path)
        elif browser_type.lower() == 'chrome':
            self._driver = webdriver.Chrome(driver_path)
        else:
            raise Exception('wrong browser type!')
        self._driver.maximize_window()

    def open_url(self, url):
        self._driver.get(url)

    def click(self, locator):
        element = self.locate_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.locate_element(locator)
        return element.text

    def get_element_attr(self, locator, attr):
        element = self.locate_element(locator)
        return element.get_attribute(attr)

    def scroll_to_element(self, element):
        self._driver.execute_script('arguments[0].scrollIntoView();', element)
    #     flag = element.location_once_scrolled_into_view()
    #     if flag is None:
    #         raise Exception('the element is not visible!')

    def click_element_by_js(self, locator):
        ele = self.locate_element(locator)
        self._driver.execute_script('$(arguments[0]).click()', ele)
