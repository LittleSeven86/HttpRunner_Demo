#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :get_all_files.py
    @Time      :2023/7/9 20:50
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
import os


def get_all_files(file_path, yaml_data_switch=False) -> list:
    """
    获取当前路径下所有的文件
    :param file_path: 目录路径
    :param yaml_data_switch: 是否过滤文件为 yaml格式， True则过滤
    :return:
    os.walk(file_path)
    作用是：遍历文件夹及其子文件夹的函数，接受一个位置参数，表示要遍历的目录路径
    :return 生成器，包括三个元素：当前文件夹的路径、当前文件夹中子文件夹的名称列表、当前文件夹文件的名称列表
    """
    filename = []
    # 获取所有文件下的子文件名称
    for current_path, current_sub_dir, current_dir_list in os.walk(file_path):
        for _file_path in current_dir_list:
            path = os.path.join(current_path, _file_path)
            # 是否过滤文件为 yaml格式， True则过滤
            if yaml_data_switch:
                if 'yaml' in path or '.yml' in path:
                    filename.append(path)
            else:
                filename.append(path)
    return filename

if __name__ == '__main__':
    res = get_all_files('/Users/z.m/pythonProject/Interface_Auto_Test/utils/other_tools')
    print(res,)