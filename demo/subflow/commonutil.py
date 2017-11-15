import time


class CommonUtil(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_specified_tab(self, loc_tab):
        self.driver.click(loc_tab)
        time.sleep(5)
