'''
Collisions
    When two keys share the same hash: 
        march 6 -> hash function -> 9
        march 17 -> hash function -> 9
        1. Chaining (append to list or linked list)
            [ [('march 7', 340)],
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
              [('march 6', 310), ('march 17', 459)]
            ]
            In this case Time Complexity:
                Look up by key : O(n) (when all keys share the same hash)
        2. Linear Probing (linearly searching for an empty slot to store (key,value) pair)
            # for march 17 -> 9 is already taken so 9+1 -> 10 but size of array is 10 so move to 0 -> 0 is already taken so 1
            [ ('march 7', 340),
              ('march 17', 459),
                ,
                ,
                ,
                ,
                ,
                ,
                ,
              ('march 6', 310)
            ]
'''
# Chaining 
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        # case where just value changed ('march 6',310) is changed to ('march 6', 200)
        for index,tuple in enumerate(self.arr[h]): 
            if len(tuple) == 2 and tuple[0]==key:
                # overwrite with a tuple with new value
                self.arr[h][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for tuple in self.arr[h]:
            if tuple[0] == key:
                return tuple[1]
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,tuple in enumerate(self.arr[h]):
            if tuple[0] == key:
                del self.arr[h][index] 

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 310
    t['march 17'] = 459
    t['march 7'] = 340
    print(t.arr)
    print(t['march 17'])
    del t['march 17']
    print(t.arr)