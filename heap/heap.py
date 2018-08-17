import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)

    self.size += 1

    self._bubble_up(self.size)

  def delete(self):
    if self.size == 0:
      return None

    old_head = self.storage.pop(0)
    new_head = self.storage.pop()
    self.size -= 1
    self.storage.insert(0, new_head)
    return old_head

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size
    

  def _bubble_up(self, index):
    if self.storage[index] > self.storage[math.floor(index/ 2)]:
      hold_num = self.storage[math.floor(index/ 2)]
      self.storage[math.floor(index/ 2)] = self.storage[index]
      self.storage[index] = hold_num

  def _sift_down(self, index):
    parent = self.storage[index]
    left_tree = self.storage[(2*index) + 1]
    right_tree = self.storage[(2*index) + 2]

    if left_tree < right_tree:
      bigger = right_tree
      right_tree = parent
      parent = bigger
    else:
      bigger = left_tree
      left_tree = parent
      parent = bigger




    
