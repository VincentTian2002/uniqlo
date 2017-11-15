from robot.api import logger


class OpenBrowser(object):
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, browser_type, url):
        assert browser_type, 'Please provide browser type!'
        self.driver.open_browser(browser_type)
        logger.info('opened ie browser!', False)
        self.driver.open_url(url)
