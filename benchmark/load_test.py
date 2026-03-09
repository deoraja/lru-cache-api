from cache.cache_service import CacheService


service = CacheService()

print(service.get_data(1))
print(service.get_data(1))
print(service.get_data(2))
print(service.get_data(1))