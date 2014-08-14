"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            return self.cache.pop(key)
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            self.cache.pop(queue.pop(0))
            self.cache[key] = value

        self.queue.append(key)
        self.cache[key] = value

    # Checked online, so changed to use python's ordered dictionary
    # So obsoleted queue
