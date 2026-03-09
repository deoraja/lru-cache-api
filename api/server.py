from fastapi import FastAPI
from cache.cache_service import CacheService

app = FastAPI()
service = CacheService()

@app.get("/data/{key}")
def get_data(key: int):

    value = service.get_data(key)

    return { "key": key, "value": value}