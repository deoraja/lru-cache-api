from locust import HttpUser, task, between
import random

class CacheUser(HttpUser):

    wait_time = between(1, 2)

    keys = [1,2,3,4,5]

    @task
    def get_cache(self):
        key = random.choice(self.keys)
        self.client.get(f"/data/{key}")