import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.size + 1)
    self.size += 1

  def delete(self):
    if self.size >= 1:
      deleted = self.storage.pop(1)
      self.storage.insert(1, self.storage[self.size-1])
      self._sift_down(1)
      self.size -= 1
      return deleted

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while (index // 2) > 0:  # parent index > 0
      if self.storage[index] > self.storage[index // 2]:  # child > parent
        temp = self.storage[index//2]  # temp = parent
        self.storage[index // 2] = self.storage[index]  # parent = child
        self.storage[index] = temp  # child = parent
      index = index // 2  # go up one level
    return

  def _sift_down(self, index):
    while (index * 2) < self.size:  # child < size
      if self.storage[index] < self.storage[index * 2]:
        old_child = self.storage[index * 2]
        self.storage[index * 2] = self.storage[index]
        self.storage[index] = old_child

      if self.storage[index] < self.storage[index * 2 + 1]:
        old_child = self.storage[index * 2 + 1]
        self.storage[index * 2 + 1] = self.storage[index]
        self.storage[index] = old_child
      index = index + 1
    pass
