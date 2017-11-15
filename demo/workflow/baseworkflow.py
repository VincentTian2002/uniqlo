from util.webdriverfunc import WebDriverFunc
from util.propertiesread import PropertiesRead
from subflow.openbrowser import OpenBrowser
from subflow.selectproduct import SelectProduct
from subflow.editproductdetails import EditProductDetails


class BaseWorkFlow(object):
    def __init__(self):
        self.driver = WebDriverFunc()
        self.test_data = {}

    def get_test_data(self, data_file):
        properties_read = PropertiesRead()
        self.test_data = properties_read.get_test_data_from_properties_file(data_file)

    def customer_open_uniqlo(self):
        assert self.test_data['browser_type'], 'please provide browser type!'
        assert self.test_data['url'], 'please provide url!'
        browser_open = OpenBrowser(self.driver)
        browser_open.open_browser(self.test_data['browser_type'], self.test_data['url'])

    def customer_select_product(self):
        assert self.test_data['product_type'], 'product type should not be None!'
        assert self.test_data['product_subtype'], 'product subtype should not be None!'
        select_product = SelectProduct(self.driver)
        select_product.select_specified_product_type(
            self.test_data['product_type'], self.test_data['product_subtype']
        )
        assert self.test_data['product_rownum'], 'product row number should not be None!'
        assert self.test_data['product_colnum'], 'product column number should not be None!'
        select_product.select_product_by_row_col(
            self.test_data['product_rownum'], self.test_data['product_colnum']
        )

    def customer_edit_product_details(self):
        assert self.test_data['product_color'], 'product color should not be None!'
        assert self.test_data['product_size'], 'product size should not be None!'
        assert self.test_data['product_quantity'], 'product quantity should not be None!'
        edit_product_details = EditProductDetails(self.driver)
        edit_product_details.wait_product_img_display()
        edit_product_details.select_product_color(self.test_data['product_color'])
        edit_product_details.select_product_size(self.test_data['product_size'])
        edit_product_details.select_quantity_by_value(self.test_data['product_quantity'])
        edit_product_details.click_add_to_cart_btn()