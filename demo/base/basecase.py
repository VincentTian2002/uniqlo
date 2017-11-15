from ..util.webdriverfunc import WebdriverFunc
from constant.commonconst import CommonConst
from robot import api

class BaseCase(object):
    # TODO
    # need to add method like:
    #   get test data from excel/db/file
    #   setup/teardown (extends unittest if needs)
    #   selenium start
    #   log relation
    #   any tools execution needs ...
    def __init__(self):
        self.driver_func = WebdriverFunc(CommonConst.BROWSER_TYPE)
