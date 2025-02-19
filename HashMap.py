'''
HashMap == HashTable
Dictionary is python's specific implementation of hash table
Java : HashMap
       LinkedHashMap
C++  : std::map 
stock_prices = {'march 6': 310.0,
                'march 7': 340.0,
                'march 8': 380.0,
                'march 9': 302.0,
                'march 10': 297.0,
                'march 11': 323.0}
march 6 -> Hash Function -> 9
march 7 -> Hash Function -> 0
stock_ prices = [340, , , , , , , , ,310]
There are different ways to implement hash function. One common method: using ASCII numbers
    m : 109
    a : 97 
    r : 114
    c : 99
    h : 104
    (space) : 32
    6 : 54
    Sum -> 609
    Size of list to store values is 10 -> 609%10 = 9
Time Complexity:
    Look up by key : O(1) on average
    Insertion/Deletion : O(1) on average
'''
# Hash Function
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        # Assume size of list is 100
        return h%self.MAX
    # Use operator module (https://docs.python.org/3/library/operator.html)
    # operator.__setitem__(a, b, c)
        #Set the value of a at index b to c
            # a[b] = c
    # t[march 6] = 130
        # t = self, key = march 6, value = 130
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    # operator.__getitem__(a, b)
        # Return the value of a at index b.
            # return a[b]
        # return t[key]
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    # operator.__delitem__(a, b)
        # Remove the value of a at index b
            # del a[b]
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()
    print(t.get_hash('march 6'))
    t['march 6'] = 130
    print(t['march 6'])
    t['dec 17'] = 27
    del t['march 6']
    print(t['march 6'])






'''
class SimpleHashMap():
    def __init__(self,size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def hash_function(self,key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum%4
    def put(self,key,value):
        hash_code = self.hash_function(key)
        bucket = self.buckets[hash_code]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value) #Update existing key
                return
            bucket.append((key,value)) #Add new key-value pair if not found 
    def get():
        pass
    def remove():
        pass
    def display():
        pass

hashMap = SimpleHashMap(size=4)
hashMap.put("123-4567","Khin")   
hashMap.put("123-4568","Zin")
hashMap.put("123-4569","Yin")
hashMap.put("123-4570","Pyay")

'''

