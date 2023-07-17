#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
@Time    :  2022-09-13 21:50
@File    :  main-runner-hapi.py
"""
import datetime,os,traceback
from httprunner.cli import main_run
from Utils.models import NotificationType
from allure_tools.allure_report_data import AllureFileClean
from notify.wechat_notify import WeChatSend
from notify.feishu_notify import FeiShuTalkChatBot
from notify.email_notify import SendEmail,TestMetrics
from notify.ding_talk import DingTalkSendMsg
from Utils import config

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
    '''
    产出allure报告
    :param case_path:
    :return:
    '''
    main_run([
        case_path,
        "-sv",
        f"--alluredir=reports/{str(now.strftime(('%m%d%H%M【测试报告】')))}",
        # '--http-stat'
    ])

def run(case_path):
    try:
        # INFO.logger.info(
        #     """
        #                      _    _         _      _____         _
        #       __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
        #      / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
        #     | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
        #      \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
        #           |_|
        #           开始执行{}项目...
        #         """.format(config.project_name)
        # )

        main_run([
            case_path,
            "-sv",
            "--clean-alluredir",
            f"--alluredir=./reports/allure_data",
            # '--http-stat'
        ])

        """
                   --reruns: 失败重跑次数
                   --count: 重复执行次数
                   -v: 显示错误位置以及错误的详细信息
                   -s: 等价于 pytest --capture=no 可以捕获print函数的输出
                   -q: 简化输出信息
                   -m: 运行指定标签的测试用例
                   -x: 一旦错误，则停止运行
                   --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
                    "--reruns=3", "--reruns-delay=2"
                   """
        os.system(rf"allure generate ./reports/allure_data -o ./reports/allure_result --clean")

        allure_data = AllureFileClean.get_case_count()
        # 2023-07-04 对allure生成的测试数据进行清洗
        notification_mapping = {
            NotificationType.DING_TALK.value: DingTalkSendMsg(allure_data).send_ding_notification,
            NotificationType.WECHAT.value: WeChatSend(allure_data).send_wechat_notification,
            NotificationType.EMAIL.value: SendEmail(allure_data).send_main,
            NotificationType.FEI_SHU.value: FeiShuTalkChatBot(allure_data).post
        }

        # 2023-07-04 默认的通知参数为0，可以在config文件中对通知类型进行设置
        if config.notification_type != NotificationType.DEFAULT.value:
            notification_mapping.get(config.notification_type)()

        # 可根据config中的配置项，失败测试用例重写
        # if config.excel_report:
        #     ErrorCaseExcel().write_case()

        # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
        # os.system(f"allure serve ./report/tmp -h 127.0.0.1 -p 9999")

    except Exception:
        # 如有异常，相关异常发送邮件
        e = traceback.format_exc()
        send_email = SendEmail(AllureFileClean.get_case_count())
        send_email.error_mail(e)
        raise


if __name__ == '__main__':
    run('/Users/z.m/pythonProject/HttpRunner_demo/demo/testcases/接口关联demo')
    # os.system(rf"allure generate ./reports/allure_data -o ./reports/allure_result --clean")
