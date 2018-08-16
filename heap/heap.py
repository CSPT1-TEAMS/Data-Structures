import math

class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
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

    print('in insert, value:', value)
    print('in insert, storage:', self.storage)

    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    removed = self.storage.pop(1)
    self.size -= 1
    self.storage.insert(1, self.storage.pop())
    self._sift_down(1)

  def _bubble_up(self, current_index):
    print('in bubble up, current_index:', current_index)

    parent_index = Heap.get_parent_index(current_index)
    print('in bubble up, parent_index:', parent_index)

    if current_index == parent_index:
      return
    

    parent = self.storage[parent_index]
    current = self.storage[current_index]
    print('in bubble up, parent:', parent)
    print('in bubble up, child:', current)

    #if parent is not None and current > parent:
    if current > parent:
      self.storage[current_index], self.storage[parent_index] = parent, current

      print('current > parent, storage:', self.storage)

      self._bubble_up(parent_index)

  def _sift_down(self, index):
    parent = self.storage(index)
    left = Heap.get_left_child_index(index)
    right = Heap.get_right_child_index(index)
    child = left if left > right else right
    child_index = self.storage.index(child)

    if parent < child:
      self.storage[child_index], self.storage[index] = parent, child
      self._sift_down(child_index)


test_heap = Heap()
test_heap.insert(100)

print('\n')

test_heap.insert(19)

print('\n')

test_heap.insert(21)

print('\n')

test_heap.insert(47)

print('\n')

test_heap.insert(35)

print('\n')

test_heap.insert(4)

print('\n')

test_heap.insert(29)

