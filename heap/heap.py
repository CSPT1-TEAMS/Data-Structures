import math
class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up( self.size + 1)
    self.size += 1
    # print('storage insert', self.storage)
    pass

  def delete(self):
    if self.size >= 1:
      deleted = self.storage.pop(1)
      print('delete', deleted)
      self._sift_down(self.size - 1)
      print('storage', self.storage)
      self.size -= 1
      return deleted

  def get_max(self):
    print('max', self.storage[1])
    return self.storage[1]

  def get_size(self):
    print('size', self.size)
    return self.size

  def _bubble_up(self, index):
    while (index // 2) > 0: #parent index > 0
      if self.storage[index] > self.storage[index//2]: #child > parent
        temp = self.storage[index//2] #temp = parent
        self.storage[index // 2] = self.storage[index] #parent = child
        self.storage[index] = temp #child = parent
      index = index // 2 #go up one level

  def _sift_down(self, index):
    while (index // 2) > 0:
      if self.storage[index] < self.storage[index//2]:
        temp = self.storage[index//2]
        self.storage[index // 2] = self.storage[index]
        self.storage[index] = temp
      index = index // 2
    pass
