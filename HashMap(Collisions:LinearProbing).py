'''
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
class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX
    def find_slot(self,key,hash):
        '''
        another way to find index
        * -> unpacking range into list
        prob_range = [*range(hash+1,self.MAX)] + [*range(0,hash)]
        for index in prob_range:
        '''
        flag = True
        index = (hash)%self.MAX
        # hash : 9
            # index : 0 1 2 3 4 5 6 7 8
        for _ in range(self.MAX):
            # found the empty slot
            if self.arr[index] is None:
                return index
            # case where just value changed ('march 6',310) is changed to ('march 6', 200)
            if self.arr[index][0] == key:
                return index
            index = (index+1)%self.MAX
        # flag for HashMap full case
        flag = False
        return flag
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,value)
        else:
            new_h = self.find_slot(key,h)
            if new_h == False:
                raise Exception("HashMap full")
            self.arr[new_h] = (key,value)
    def __getitem__(self,key):
        hash = self.get_hash(key)
        # case where there is no element with the key
        if self.arr[hash] is None:
            return
        index = self.find_slot(key,hash)
        if index == False:
            return
        return self.arr[index][1]
    def __delitem__(self,key):
        hash = self.get_hash(key)
        # case where there is no element with the key
        if self.arr[hash] is None:
            return
        index = self.find_slot(key,hash)
        self.arr[index] = None
         

if __name__ == '__main__':
    hm = HashMap()
    print(hm.get_hash('may 7'))
    hm['march 7'] = 349 #hash value = 0
    hm['march 6'] = 310 #hash value = 9
    hm['march 17'] = 459 #hash value = 9
    hm['march 17'] = 300
    hm['nov 1'] = 22 #hash value = 0
    hm['april 1'] = 1 #hash value = 7
    hm['april 2'] = 2 #hash value = 8
    hm['april 3'] = 3 #hash value = 9
    hm['april 4'] = 4 #hash value = 0
    hm['may 22'] = 89 #hash value = 9
    hm['may 7'] = 183 #hash value = 4
    print(hm['march 17'])
    print(hm['dec 1']) # hash value 1
    # hm['jan 1'] = 0 # HashMap full error
    del hm['april 2']
    print(hm.arr)
    hm['jan 1'] = 0
    print(hm.arr)