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
