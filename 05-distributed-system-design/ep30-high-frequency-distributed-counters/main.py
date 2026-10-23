# Phase 1: Probabilistic Early Expiration (XFetch Pattern)
import random
import math
import time

def xfetch_read(key: str, beta: float = 1.0):
    '''Prevents cache stampedes by recomputing before expiration probabilistically.'''
    val, delta, ttl = redis_client.get_with_meta(key)
    if not val or (time.time() - (delta * beta * math.log(random.random()))) >= ttl:
        new_val = recompute_expensive_query(key)
        redis_client.set(key, new_val, ttl=300)
        return new_val
    return val
