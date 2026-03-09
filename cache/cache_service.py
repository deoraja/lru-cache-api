from cache.lru_cache import LRUCache
from database.postgres_db import PostgresDatabase


class CacheService:

    def __init__(self):

        #small capacity for testing eviction
        self.cache = LRUCache(3)

        #databse connection simultation
        self.db = PostgresDatabase()

    def get_data(self,key):

        #check cache first
        value = self.cache.get(key)

        if value != -1:
            print("CACHE HIT")
            return value
        #cache miss
        print("CACHE MISS -> fetching from DB")
        
        value = self.db.get(key)

        if value is not None:
            self.cache.put(key, value)

        return value