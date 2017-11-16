import time
from robot.api import logger
from demo.constant.page_locator.productlistpage import ProductListPage
from demo.constant.page_locator.homepage import HomePage


class SelectProduct(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage()
        self.product_page = ProductListPage()

    def select_specified_product_type(self, head_type, sub_type):
        loc_head_type = self.home_page.HEAD_PRODUCT.format(head_type.upper())
        ele_head_type = self.driver.locate_element(loc_head_type)
        # click parent element first because driver lost the focus, then click element
        # or we can try to fix this using execute_script
        # parent_ele = self.driver.locate_element_by_element(ele_head_type, 'xpath=./..')
        # parent_ele.click()
        self.driver.click(self.home_page.UNIQLO_LOGO)

        self.driver.click(loc_head_type)
        time.sleep(3)
        loc_sub_type = self.home_page.SUB_PRODUCT.format(head_type.lower(), sub_type)
        flag = self.driver.wait_util_element_exist(loc_sub_type)
        if flag:
            # ele_sub_type = self.driver.locate_element(loc_sub_type)
            # parent_ele = self.driver.locate_element_by_element(ele_sub_type, 'xpath=./..')
            # parent_ele.click()
            self.driver.click(loc_sub_type)
            logger.info('selected product type successfully!')
        else:
            logger.error('time out! cannot find subtype on the page.')

    def select_product_by_row_col(self, row_number, col_number):
        flag = self.driver.wait_util_element_exist(self.product_page.PRODUCTS_ROWS)
        if flag:
            products_rows = self.driver.locate_elements(self.product_page.PRODUCTS_ROWS)
        else:
            logger.error('time out! cannot find product row element.')
        if int(row_number) > len(products_rows):
            raise Exception('row number is out of the range of product rows.')
        else:
            product_row = products_rows[int(row_number)-1]
        products_cols = \
            self.driver.locate_elements_by_element(product_row, self.product_page.PRODUCTS_COLUMNS)
        if int(col_number) > len(products_cols):
            raise Exception('column number is out of the range of product columns!')
        else:
            product = products_cols[int(col_number)-1]
        self.driver.click(self.product_page.TEXT_SEARCH)
        self.driver.scroll_to_element(product)
        # print product.get_attribute('title')
        product.click()
