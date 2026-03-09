from cache.node import Node
import time

class LRUCache:
    def __init__(self,capacity: int):
      self.capacity = capacity
      self.cache = {}
      
      self.hits = 0
      self.misses = 0

      self.head = Node(0,0)  
      self.tail = Node(0,0)  

      self.head.next = self.tail
      self.tail.prev = self.head

    #disconnet node
    def _remove(self, node: Node):
      prev_node = node.prev
      next_node = node.next

      prev_node.next = next_node
      next_node.prev = prev_node

    # <head>...list...<tail> fixed dummy nodes head and tail 
    def _insert(self, node: Node):
      next_node = self.head.next
      self.head.next = node
      node.prev = self.head
      node.next = next_node
      next_node.prev = node


    def get(self, key: int):
      if key not in self.cache:
       self.misses += 1
       return -1
      
      self.hits += 1
      node = self.cache[key]
      
      # detach node from current position (node object reference still exists)
      self._remove(node)

      # reinsert at front to mark as most recently used
      self._insert(node)

      return node.value

    def put(self, key:int, value:int):
   
     #cache hit
      if key in self.cache:
         node = self.cache[key]
         node.value = value

         self._remove(node)
         self._insert(node)

      #cache miss onwards
      else:
         if len(self.cache) >= self.capacity:  
          #remove LRU node
          lru = self.tail.prev
          self._remove(lru)
          del self.cache[lru.key]

      new_node = Node(key, value)

      self.cache[key] = new_node
      self._insert(new_node)

    def get_metrics(self):
      total = self.hits + self.misses
      hit_rate = self.hits / total if total>0 else 0
      return{
        "hits": self.hits,
        "misses" : self.misses,
        "hit_rate": hit_rate 
      }
    

   


   