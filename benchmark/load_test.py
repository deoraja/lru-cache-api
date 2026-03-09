from cache.lru_cache import LRUCache

cache = LRUCache(2)

cache.put(1,"A")
cache.put(2,"B")

print(cache.get(1)) # A

cache.put(3,"A") # evicts 2 

print(cache.get(2))  # -1 (not found)
print(cache.get_metrics())
