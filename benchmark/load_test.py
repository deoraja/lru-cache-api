from cache.cache_service import CacheService
import time

service = CacheService()

#DB
start = time.time()
service.get_data(1)
end = time.time()

db_time = end - start
print("\nDB Response Time:", db_time)

#cache
start = time.time()
service.get_data(1)
end = time.time()

cache_time = end - start
print("\nCache Response Time:", cache_time)

#speedup
speedup = db_time / cache_time
print("\nCache is", round(speedup,2),"x faster than DB")
