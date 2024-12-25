"""
Building an HashMap Class, to have the following:
get_hash()
__getitem__
__setitem__
del_item()

Then build a Chain HashMap
"""

class HashMap():
    def __init__(self):
        self.MAX = 50
        self.array = ["" for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.array[hash]
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.array[hash] = value
        
    def __del_item__(self, key):
        hash = self.get_hash(key)
        del self.array[hash] # or self.array[hash] = ""
        

class ChainMap():
    def __init__(self):
        self.MAX = 10
        self.array = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for i in self.array[hash]:
            if i[0] == key:
                return i[1]
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        for index, element in enumerate(self.array[hash]):
            if len(element) == 2 and element[0] == key: # checks if list contains more than two elements, and identifies if key matches
               self.array[hash][index] = (key,value)
               return
        self.array[hash].append((key, value))
        
        
# Test cases for ChainMap implementation
chain_map = ChainMap()

# Test 1: Basic Insertion and Retrieval
chain_map["name"] = "Alice"
chain_map["age"] = 25
print(chain_map["name"])  # Expected: Alice
print(chain_map["age"])   # Expected: 25

# Test 2: Update Existing Key
chain_map["name"] = "Bob"  # Update value
print(chain_map["name"])  # Expected: Bob

# Test 3: Handling Collisions
chain_map["abc"] = "Value1"  # Assume "abc" and "cba" hash to the same bucket
chain_map["cba"] = "Value2"
print(chain_map["abc"])  # Expected: Value1
print(chain_map["cba"])  # Expected: Value2

# Test 4: Retrieve Non-Existent Key
try:
    print(chain_map["nonexistent"])  # Should raise an error or return None (depending on design)
except KeyError:
    print("Key not found!")  # Expected output

# Test 5: Large Number of Keys
for i in range(50):
    chain_map[f"key{i}"] = f"value{i}"
print(chain_map["key0"])  # Expected: value0
print(chain_map["key49"])  # Expected: value49
print(chain_map["key25"])  # Expected: value25

# Test 6: Duplicate Keys in Same Bucket
chain_map["abc"] = "FirstValue"
chain_map["abc"] = "UpdatedValue"
print(chain_map["abc"])  # Expected: UpdatedValue

