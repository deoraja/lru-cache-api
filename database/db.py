import time

class FaksDatabase:

    def __init__(self):
        
        self.data = {
            1: "Apple",
            2: "Banana",
            3: "Mango",
            4: "Orange"
        }
    
    def get(self, key):
        
        # simulate slow database query
        time.sleep(0.2)
        return self.data.get(key)