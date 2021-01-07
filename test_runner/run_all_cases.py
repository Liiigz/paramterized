
import unittest
import os
from utils import HTMLTestReportCN
from utils.config_utils import local_config
casepath = os.path.join(os.path.dirname(__file__), '..','testcase')#测试报告路径
result_path=os.path.join(os.path.dirname(__file__),'..',local_config.REPORT_PATH)

def load_testcase():
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                                       pattern='test_api_case.py',
                                                       top_level_dir=casepath)
    all_case_suite = unittest.TestSuite()
    all_case_suite.addTest(discover)
    return all_case_suite


result_dir = HTMLTestReportCN.ReportDirectory(result_path)  # 创建一个测试报告路径对象
result_dir.create_dir('test_framwork')  # 调用创建目录方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')  # 获取测试报告文件的路径 此处必须填report_path
report_html_obj = open(report_html_path, 'wb')
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_obj,
                                                      title='接口测试报告',
                                                      description='数据驱动和关键字驱动',
                                                      tester='Liiigz'
                                                      )
html_runner.run(load_testcase())
report_html_obj.close()
