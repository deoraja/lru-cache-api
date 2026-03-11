from cache.lru_cache import LRUCache
from database.postgres_db import PostgresDatabase
import logging

logger = logging.getLogger("cache_service")

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
            logger.info(f"CACHE HIT: {key}")
            return value
        #cache miss
        logger.info(f"CACHE MISS: {key} | fetching from DB")
        
        value = self.db.get(key)

        if value is not None:
            logger.info(f"DB FETCH: {key}")
            self.cache.put(key, value)

        return value