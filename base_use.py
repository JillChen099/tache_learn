#  -*- coding: utf-8 -*-
"""
Created on 2018/3/31 11:07

@author: ChenJinLong

@Email: 714178326@qq.com

@Content: 
"""

import random
import fakeredis
from tache import RedisCache
redis_client = fakeredis.FakeStrictRedis()
cache = RedisCache(conn=redis_client, format="JSON")

@cache.cached()
def add(a, b):
    return a + b + random.randint(1,100)

result1 = add(5, 6)
result2 = add(5, 6)
print(result1,result2)
# 缓存生效值不变
assert add(5, 6) == result1
# # 失效缓存
add.invalidate(5, 6)


result3 = add(5,6)  #重新生成缓存
result4 = add(5,6)
print(result3,result4)
assert add(5, 6) != result1