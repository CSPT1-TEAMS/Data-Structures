class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # add to array
    self.storage.append( value )
    # # update size
    self.size += 1
    # bubble _bubble_up
    self._bubble_up( self.size  )

  def delete(self):
    # save value
    # swap first and last elements
    # delete array
    # sift down
    # update dize
    # return value
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.storage.pop()
    self.size -= 1
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]
    # should be one line...where can we A:WAYS
    # find the biggest value
  def get_size(self):
    # return self.size
    return self.size

  def _bubble_up(self, index):
    parent_index = index // 2
    child = self.storage[index]
    parent = self.storage[parent_index]

    if child > parent and parent != 0:
      self.storage[index] = parent
      self.storage[parent_index] = child
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    # insert last element at (empty) root
    # while index < its children
      #swap
      while (index * 2) <= self.get_size():
        min_child = self.get_min_child(index)
        if self.storage[index] < self.storage[min_child]:
          self.storage[index], self.storage[min_child] = self.storage[min_child], self.storage[index]
        else:
          break
        index = min_child

  def get_min_child(self, index):
    left = index * 2
    right = index * 2  + 1
    if right > self.get_size():
          return left
    else:
      if self.storage[left] > self.storage[right]:
        return left
      else:
        return right


