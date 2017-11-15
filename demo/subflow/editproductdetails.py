import time
from robot.api import logger
from constant.page_locator.productdetailspage import ProductDetailsPage
from constant.colorcode import ColorCode


class EditProductDetails(object):
    def __init__(self, driver):
        self.driver = driver
        self.product_details_page = ProductDetailsPage()

    def wait_product_img_display(self):
        flag = self.driver.wait_util_element_exist(self.product_details_page.PRODUCT_IMG)
        if flag:
            logger.info('product image loaded successful!')
        else:
            logger.error('product image loaded failed!')

    def select_product_color(self, color):
        loc_color = self.product_details_page.PRODUCT_COLOR.format(color.upper())
        if self.driver.element_is_exist(loc_color):
            logger.info('found locator for color: %s.' % color.upper())
        else:
            logger.error('cannot found locator for color: %s' % color.upper())
        self.driver.click(loc_color)
        self.assert_color_and_code(color)

    def assert_color_and_code(self, color):
        text_color_id = self.driver.get_text(self.product_details_page.PRODUCT_COLOR_ID)
        combine_text = '%s %s' % (ColorCode().COLOR_CODE_RELATION[color.upper()], color.upper())
        if combine_text in text_color_id:
            logger.info('color:{}, id:{}'.format(color.upper(), ColorCode().COLOR_CODE_RELATION[color.upper()]))
        else:
            logger.error('color or id is not correct!')

    def select_product_size(self, size):
        loc_size = self.product_details_page.PRODUCT_SIZE.format(size.upper())
        self.driver.click(loc_size)

    def select_quantity_by_value(self, quantity):
        self.driver.select_from_drop_down_list(value=quantity)

    def click_add_to_cart_btn(self):
        flag = self.driver.element_is_enabled(self.product_details_page.ADD_TO_CART_BUTTON)
        if flag:
            self.driver.click(self.product_details_page.ADD_TO_CART_BUTTON)
            time.sleep(3)
            logger.info('add to cart button is enabled! clicked this button.')
        else:
            logger.error('add to cart button is disabled!')
