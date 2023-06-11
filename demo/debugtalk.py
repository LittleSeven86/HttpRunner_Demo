import logging
import time
from typing import List
import os, yaml.scanner


# commented out function will be filtered
# def get_headers():
#     return {"User-Agent": "hrp"}
import pymysql

config_file = "./config.yml"


def get_user_agent():
    return "hrp/funppy"


def sleep(n_secs):
    time.sleep(n_secs)


def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def sum_ints(*args: List[int]) -> int:
    result = 0
    for arg in args:
        result += arg
    return result


def sum_two_int(a: int, b: int) -> int:
    return a + b


def sum_two_string(a: str, b: str) -> str:
    return a + b


def sum_strings(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


def concatenate(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += str(arg)
    return result


def setup_hook_example(name):
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"


def teardown_hook_example(name):
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"


def get_mobilephone_pwd(a, b):
    list = []
    for num in range(a, b):
        info = ['133000000' + str(num), 'Aa123456']
        list.append(info)
    return list


def hook_print(msg):
    print(msg)


def setup_hook_add_kwargs(request):
    request["key"] = "value"


def setup_hook_remove_kwargs(request):
    request.pop("key")


def teardown_hook_sleep_N_secs(response, n_secs):
    """sleep n seconds after request"""
    if response.status_code == 200:
        time.sleep(0.1)
    else:
        time.sleep(n_secs)


def connect_database(filepath,sql):
    if os.path.exists(filepath):
        config_data = open(filepath, 'r', encoding='utf-8')
        res = yaml.load(config_data, Loader=yaml.FullLoader)
    else:
        raise FileNotFoundError('can`t found File')

    # print(type(res['sql_db']))
    # connection = pymysql.connect(host='api.lemonban.com',user='future',password='123456',database='future')
    try:
        connection = pymysql.connect(**res['sql_db'])
    except Exception as e :
        raise ConnectionError('链接失败')

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            result = cursor.fetchone()
            print(result)
    finally:
        # 关闭数据库
        connection.close()






if __name__ == '__main__':
    # print(get_mobilephone_pwd(97,100)
    print(connect_database("./config.yml"))
