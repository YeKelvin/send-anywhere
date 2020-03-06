#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : config.py
# @Time    : 2019/3/15 10:54
# @Author  : Kelvin.Ye
import configparser
import os
from sendanywhere.utils.path_util import RESOURCES_PATH

# 项目配置路径
CONFIG_PATH = os.path.join(RESOURCES_PATH, 'config.ini')


def get(section: str, key: str, filepath: str = CONFIG_PATH) -> str:
    """获取配置文件中的属性值，默认读取config.ini

    Args:
        section: section名
        key: 属性名
        filepath: 配置文件路径

    Returns:
        属性值
    """
    if not os.path.exists(filepath):
        raise FileExistsError(filepath + ' 配置文件不存在')
    config = configparser.ConfigParser()
    config.read(filepath, encoding='utf-8')
    return config.get(section, key)
