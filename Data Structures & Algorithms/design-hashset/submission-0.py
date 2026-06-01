class MyHashSet:

    def __init__(self):
        self.size = 10000001
        self.bit = [False]*self.size
        

    def add(self, key: int) -> None:
        self.bit[key] = True
        

    def remove(self, key: int) -> None:
        self.bit[key] = False
        

    def contains(self, key: int) -> bool:
        return self.bit[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)