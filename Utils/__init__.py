#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :__init__.py.py
    @Time      :2023/7/9 20:49
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
from Utils.yaml_control import GetYamlData
from common.setting import ensure_path_sep
from Utils.models import Config


_data = GetYamlData(ensure_path_sep("\\common\\config.yml")).get_yaml_data()
config = Config(**_data)
# print(config)
