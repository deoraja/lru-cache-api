from fastapi import FastAPI
from cache.cache_service import CacheService
from core.logging import setup_logging
import logging


setup_logging()

app = FastAPI()

service = CacheService()

logger = logging.getLogger("api")

@app.get("/data/{key}")
def get_data(key: int):

    logger.info(f"API REQUEST for key: {key}")
    value = service.get_data(key)
    return { "key": key, "value": value}

@app.get("/metrics")
def metrics():
    logger.info("METRICS REQUESTED")
    return service.cache.get_metrics()