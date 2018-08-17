import math

class Heap:
  def __init__(self):
    # Storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  @staticmethod
  def get_left_child_index(parentIndex):
    return 2 * parentIndex

  @staticmethod
  def get_right_child_index(parentIndex):
    return 2 * parentIndex + 1

  @staticmethod
  def get_parent_index(child_index):
    # prevent replacing max value with 0 index (0)
    if child_index == 1:
      return child_index
    return math.floor(child_index / 2)

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    removed = self.storage.pop(1)
    new_head = self.storage.pop()
    self.size -= 1
    self.storage.insert(1, new_head)
    self._sift_down(1)
    return removed

  def _bubble_up(self, current_index):
    parent_index = Heap.get_parent_index(current_index)
    if current_index == parent_index:
      return

    parent = self.storage[parent_index]
    current = self.storage[current_index]
    if current > parent:
      self.storage[current_index], self.storage[parent_index] = parent, current
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    size = self.get_size()
    # Base case:
    # This check avoids an edge case where the test tries to delete 0 from [0]
    if(size == 0):
      return

    parent = self.storage[index]
    left_index = Heap.get_left_child_index(index)
    right_index = Heap.get_right_child_index(index)

    # Test to make sure left index isn't out of range:
    if left_index <= size:
      left = self.storage[left_index]
    else:
      left = float('-inf')

    # Test to make sure right index isn't out of range:
    if right_index <= size:
      right = self.storage[right_index]
    else:
      right = float('-inf')

    # Base case: If both children are -infinity, the node has no
    # children and we need to bail out:
    if math.isinf(left) and math.isinf(right):
      return

    child = left if left > right else right
    child_index = self.storage.index(child)

    if parent < child:
      self.storage[child_index], self.storage[index] = parent, child
      self._sift_down(child_index)
    else:
      # Base case: If parent is greater than child, out heap is balanced.
      return

