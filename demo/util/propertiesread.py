import os
from demo.constant.commonconst import CommonConst


class PropertiesRead(object):
    def __init__(self):
        self.constant = CommonConst()

    def get_test_data_from_properties_file(self, file_name):
        test_data = {}
        file_path = self.get_test_data_file(file_name)
        # file_path = os.path.realpath('test.properties')
        lines = open(os.path.realpath(file_path))
        try:
            for line in lines:
                line = line.replace('\n', '')
                if line.startswith('#') or line == '':
                    continue
                pattern = line.split('=', 1) if '=' in line else []
                if not (all(pattern) and pattern):
                    raise Exception('test data: "{}" is not the right format!'.format(line))
                test_data[pattern[0]] = pattern[1]
        finally:
            lines.close()
        return test_data

    def get_test_data_file(self, file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        combine_path = '%s/%s' % (CommonConst.TEST_DATA_PATH, file_name)
        data_file_path = os.path.join(os.path.dirname(dir_path), combine_path)
        return data_file_path
