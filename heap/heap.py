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
    self.storage[1], self.storage[self.size] = self.storage[self.size], self.storage[1]
    val = self.storage.pop(-1)
    self.size -= 1
    self._sift_down(1)
    return val

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    if (self.storage[index] < self.storage[math.floor(index / 2)]) or (index <= 1):
      return
    else:
      tmp = self.storage[index]
      self.storage[index] = self.storage[math.floor(index / 2)]
      self.storage[math.floor(index / 2)] = tmp
      return self._bubble_up(math.floor(index / 2))

  def _sift_down(self, index):
    if self.size < 2 * index:
      return
    elif self.size < 2 * index + 1:
      if self.storage[index] < self.storage[2 * index]:
        self.storage[index], self.storage[2 * index] = self.storage[2 * index], \
                                                       self.storage[index]
        return
    else:
      if self.storage[2 *index] < self.storage[2 * index + 1]:
        if self.storage[index] < self.storage[2 * index + 1]:
          self.storage[index], self.storage[2 * index + 1] = self.storage[2 * index + 1], \
                                                             self.storage[index]
          return self._sift_down(2 * index + 1)
        else:
          return
      else:
        if self.storage[index] < self.storage[2 * index]:
          self.storage[index], self.storage[2 * index] = self.storage[2 * index], \
                                                             self.storage[index]
          return self._sift_down(2 * index)
        else:
          return
