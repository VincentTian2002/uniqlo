from workflow.baseworkflow import BaseWorkFlow


def demo():

    bf = BaseWorkFlow()
    bf.get_test_data('test.properties')
    bf.customer_open_uniqlo()
    bf.customer_select_product()
    bf.customer_edit_product_details()


if __name__ == '__main__':
    demo()
