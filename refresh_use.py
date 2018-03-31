#  -*- coding: utf-8 -*-
"""
Created on 2018/3/31 11:48

@author: ChenJinLong

@Email: 714178326@qq.com

@Content: 
"""

import random
import fakeredis
from tache import RedisCache
redis_client = fakeredis.FakeStrictRedis()
cache = RedisCache(conn=redis_client, format="JSON")


class A(object):

    def __init__(self):
        self.extra = 0

    @cache.cached()
    def add(self, a, b):
        self.extra += 1
        return a + b + self.extra

a = A()
assert a.add(5, 6) == 12
assert a.extra == 1
assert a.add.refresh(5, 6) == 13 #过期并重新生成新值
assert a.extra == 2