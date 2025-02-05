class HashMap:
    #Initialization of size
    def __init__(self, capacity = 32):
        self.list = []
        for i in range(capacity):
            self.list.append([])

    #Get function(cited from WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py)
    def get(self, key):
        store = hash(key) % len(self.list)
        place = self.list[store]

        for k in place:
            if key == k[0]:
                return k[1]
        return None  #key not found

    #Add & Update function
    def insert(self, key, item):
        #get list
        store = hash(key) % len(self.list)
        store_key = self.list[store]

        #update list if already in bucket
        for k in store_key:
            if k[0] == key:
                k[1] = item
                return True

        #add to list
        key_val = [key, item]
        store_key.append(key_val)
        return True

    #delete function
    def remove(self, key):
        store = hash(key) % len(self.list)
        place = self.list[store]

        if key in place:
            place.remove(key) #key not found