#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os



class Config:

    def __init__(self):
        pass

class DevConf(Config):
    DATABASE = {
        'name': "vm_history",
        'user': "root",
        'password': '123456',
        'host': '127.0.0.1',
        'port': '3306',

    }
    CMDB = 'http://127.0.0.1:8080'


class TestConf(Config):
    DATABASE = {
        'name': "vm_history",
        'user': "root",
        'password': '123456',
        'host': '10.128.103.150',
        'port': '3306',

    }
    CMDB = 'http://10.128.103.150:8080'


class ProConf(Config):
    DATABASE = {
        'name': "vm_history",
        'user': "root",
        'password': '123456',
        'host': '127.0.0.1',
        'port': '3306',

    }
    CMDB = 'http://127.0.0.1:8080'


ENV_CONFIG = {
    'test': TestConf,
    'pro': ProConf,
    'default': DevConf,
    'dev': DevConf,
}



CONFIG = ENV_CONFIG.get(os.environ.get('ENV_CONFIG','default'))