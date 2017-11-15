import time
from robot.api import logger
from constant.page_locator.productlistpage import ProductListPage
from constant.page_locator.homepage import HomePage


class SelectProduct(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage()
        self.product_page = ProductListPage()

    def select_specified_product_type(self, head_type, sub_type):
        loc_head_type = self.home_page.HEAD_PRODUCT.format(head_type.upper())
        self.driver.click(loc_head_type)
        time.sleep(3)
        loc_sub_type = self.home_page.SUB_PRODUCT.format(sub_type)
        flag = self.driver.wait_util_element_exist(loc_sub_type)
        if flag:
            self.driver.click(loc_sub_type)
            time.sleep(3)
            logger.info('selected product type successfully!')
        else:
            logger.error('time out! cannot find subtype on the page.')

    def select_product_by_row_col(self, row_number, col_number):
        flag = self.driver.wait_util_element_exist(self.product_page.PRODUCTS_ROWS)
        if flag:
            products_rows = self.driver_func.locate_elements(self.product_page.PRODUCTS_ROWS)
        else:
            logger.error('time out! cannot find product row element.')
        if row_number > len(products_rows):
            raise Exception('row number is out of the range of product rows.')
        else:
            product_row_locator = products_rows[row_number-1]
        products_cols = \
            self.driver_func.locate_elements_by_element(product_row_locator, self.product_page.PRODUCTS_COLUMNS)
        if col_number > len(products_cols):
            raise Exception('column number is out of the range of product columns!')
        else:
            product = products_cols[col_number-1]
        self.driver_func.scroll_to_element(product)
        time.sleep(1)
        product.click()
        time.sleep(3)
