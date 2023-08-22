

class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_item(self):

        return f"Key: {self.key}, Value: {self.value}"



class HashTable:

    def __init__(self):
        
        self.size = 2
        self.items = [None for _ in range(self.size)]
        self.count = 0

    
    def _hash(self, key):
        result = 0
        multiplier = 1

        for ch in key:
            result += multiplier * ord(ch) # reeturns the bytes of character
            multiplier += 1
        
        index = result % self.size

        return index
    
    def put(self, key, value):

        hash_item = HashItem(key, value)
        hash_index = self._hash(key)

        load_factor = self.count / self.size
        
        if load_factor >= 0.75:
            self.enlarge_size()
            
        while self.items[hash_index] is not None:

            if self.items[hash_index].key is key:
                break

            hash_index += 1

        if self.items[hash_index] is None:
            self.items[hash_index] = hash_item

        self.count += 1
                
        
    
    
    def get(self, key):

        hash_index = self._hash(key)

        while self.items[hash_index] is not None:

            if self.items[hash_index].key is key:
                return self.items[hash_index]
            
            hash_index += 1

        return None
    

    def enlarge_size(self):
        self.size *= 2
        self.items += [None for _ in range(self.size)]
    


hash_table = HashTable()

for _ in range(10):

    hash_table.put("ad", "collide")

for _ in range(10):
    print(hash_table.get("ad").get_item())


print(hash_table.count)

        


        