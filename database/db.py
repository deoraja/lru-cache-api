import time

#Implemented to test before connecting real database to check results
class FaksDatabase:

    def __init__(self):
        
        self.data = {
            1: "Test_1",
            2: "Test_2",
            3: "Test_3",
            4: "Test_4"
        }
    
    def get(self, key):
        
        # simulate slow database query
        time.sleep(0.2)
        return self.data.get(key)