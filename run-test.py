#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
@Time    :  2022-09-13 21:50
@File    :  main-runner-hapi.py
"""
import datetime
from httprunner.cli import main_run

now = datetime.datetime.now()


def run_with_lemon_report(case_path, report_path, report_title, desc, template_id):
    '''
    功能：产出柠檬班测试报告
    :param case_path: 测试用例路径
    :param report_path:报告产出路径
    :param report_title:报告标题
    :param desc:描述信息
    :param template_id:模板ID 1/2
    :return:
    '''
    main_run([
        case_path, "-sv",
        "--report=" + report_path,
        "--tester=" + report_title,
        "--desc=" + desc,
        f"--template={template_id}"])


def run_with_allure_report(case_path):
    main_run([
        case_path,
        "-sv",
        f"--alluredir=reports/{str(now.strftime(('%m%d%H%M【测试报告】')))}"
    ])


if __name__ == '__main__':
    # 使用allure测试报告
    # run_with_allure_report(r"D:\Python\Httprunner_Demo\demo\testcases\hook_demo\hook_demo.yml")

    # 使用lemon测试报告
    run_with_lemon_report(r"D:\Python\Httprunner_Demo\demo\testcases\hook_demo\hook_demo.yml","test1","xiaoqi","11",2)
