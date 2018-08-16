import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    print('value', value)
    self._bubble_up(self.size + 1)
    self.size += 1

  def delete(self):
    pass

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    # return self.size
    pass

  def _bubble_up(self, index):
    print('index//2', index//2)
    print('len', len(self.storage))
    print('storage', self.storage)
    if self.storage[index] < self.storage[ (index//2) ]:
      return
    else: #child > parent
      old_parent = self.storage[(index//2)]
      new_parent = self.storage[index]
      print('old_parent', old_parent)
      self.storage[(index//2)] = new_parent
      self.storage[index] = old_parent
      # self.storage.append(old_parent)
      # self._bubble_up(-1)
      # self.storage[index] = self._sift_down(index)
      
      print('new parent', self.storage[(index//2)])

      # self._bubble_up(self.storage[(index//2)])
      print('storage2', self.storage)
      return

  def _sift_down(self, index):
    # if self.storage[index] > self.storage[(index//2)]:
    pass
