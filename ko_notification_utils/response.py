#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/11 
=================================================='''


class Response():

    def __init__(self, code, success, data):
        self.code = code
        self.data = data
        self.success = success
