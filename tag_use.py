#  -*- coding: utf-8 -*-
"""
Created on 2018/3/31 11:42

@author: ChenJinLong

@Email: 714178326@qq.com

@Content: 
"""
import random
import fakeredis
from tache import RedisCache
redis_client = fakeredis.FakeStrictRedis()
cache = RedisCache(conn=redis_client, format="JSON")


@cache.cached(tags=["a:{0}"])
def add(a, b):
    return a + b + random.randint(1,100)

result1 = add(5, 6)
result2 = add(5, 7)

print(result1,result2)
add.invalidate_tag("a:5") #a为key,5为value,a=5的都过期，重新计算

result3 = add(5,6)
result4 = add(5,7)
print(result3,result4)

assert result1 != add(5, 6)
assert result2 != add(5, 7)