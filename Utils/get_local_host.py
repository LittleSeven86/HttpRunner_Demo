#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :get_local_host.py
    @Time      :2023/7/11 15:06
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
import socket


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    _s = None
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8', 80))
        l_host = _s.getsockname()[0]
    finally:
        _s.close()

    return l_host

if __name__ == '__main__':
    res = get_host_ip()
    print(res)