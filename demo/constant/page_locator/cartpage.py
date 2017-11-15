class CartPage(object):
    CART_TABLE = '//table[@class="cartDivideItemList"]'
    CART_ROWS = '//table[@class="cartDivideItemList"]/tbody/tr'
    CART_CELL = '//table[@class="cartDivideItemList"]/tbody/tr["{row}"]/td["{col}"]'
