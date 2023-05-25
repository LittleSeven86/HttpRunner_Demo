#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
@Time    :  2022-09-13 21:50
@Author  :  王彦青
@File    :  main-runner-hapi.py
"""
from httprunner.cli import main_run
if __name__ == '__main__':

    # -v 参数：debug模式打印出具体执行过程和请求响应出入参
    # main_run(['test/demo/testcases/测试1.yml',
    #       '-v',
    #       ])

# 可直接运行，如果想定位问题，可直接debug模式运行
    main_run([r"/Users/z.m/pythonProject/HttpRunner_demo/demo/testcases/ymlCaseDemo/Yml_demo.yml",  # case路径
              # '-v',
              # '-s',
              # '--report=hhhhhh.html',
              # '--title=【酒旅-质量保障部】自动化报告',
              # '--tester=【酒旅-质量保障部】',
              # '--desc=报告描述信息【酒旅-质量保障部】',
              # '--template=2'
              '--alluredir=reports/5'
            ])

