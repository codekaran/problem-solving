class queue:
    arr = [None,None,None,None]
    first = -1
    last = -1
    cap = 4

    def insert(self, val):
        # is full returns -1 if queue is full else: the next index to insert the value in
        print('inserting ',val)
        next_index = self.isFull()
        if next_index ==-1:
           print('Queue is full')
           return
        if self.first == -1:
            self.first+=1
        # update the last index
        self.last = next_index
        self.arr[self.last] = val
        print('first: ',self.first,'last:',self.last)
    
    def get_first(self):
        return self.arr[self.first]
    
    def get_last(self):
        return self.arr[self.last]

    def pop(self):
        print('popping index: ',self.first)
        if not self.isEmpty():
            print('Popped : ',self.arr[self.first])
            self.arr[self.first] = None
            if self.first == self.cap-1:
                self.first = self.first % (self.cap-1)
            else:
                self.first+=1

        else:
            print('is empty')
        print('first: ',self.first,'last:',self.last)

    def isEmpty(self):
        # first and last are same and the index value shuld not be None
        if self.first == self.last and not self.arr[self.first]:
            return True
        return False
    
    def isFull(self):
        # in circular queue if first and last are adjecent
        # this saves O(n) shifting of index.
        # check if last ke bad there is space
        next_index_to_check = 0
        if self.last == (self.cap-1):
            next_index_to_check = self.last % (self.cap-1) # getting the next index to insert the value
        else:
            next_index_to_check = self.last+1
        if  self.arr[next_index_to_check]:
            return -1
        else: return next_index_to_check
    def get_list(self):
        return self.arr

q=queue()
q.insert(1)
print(q.get_list())
q.insert(2)
print(q.get_list())
q.insert(3)
print(q.get_list())
q.insert(4)
print(q.get_list())
q.pop()
print(q.get_list())
q.pop()
print(q.get_list())
q.pop()
print(q.get_list())
q.pop()
print(q.get_list())
q.insert(5)
print(q.get_list())
q.pop()
print(q.get_list())
q.insert(6)
print(q.get_list())
q.insert(7)
print(q.get_first())
print(q.get_last())
print(q.get_list())