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
    #print('in insert, value:', value)
    #print('in insert, storage:', self.storage)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    removed = self.storage.pop(1)
    new_head = self.storage.pop()
    #print('in delete, deleting:', removed)
    self.size -= 1
    self.storage.insert(1, new_head)
    #print('in delete, inserting new head', new_head)
    #print('in delete, new storage', self.storage)
    self._sift_down(1)
    return removed

  def _bubble_up(self, current_index):
    #print('in bubble up, current_index:', current_index)
    parent_index = Heap.get_parent_index(current_index)
    #print('in bubble up, parent_index:', parent_index)
    if current_index == parent_index:
      return

    parent = self.storage[parent_index]
    current = self.storage[current_index]
    #print('in bubble up, parent:', parent)
    #print('in bubble up, child:', current)
    if current > parent:
      self.storage[current_index], self.storage[parent_index] = parent, current

      #print('current > parent, storage:', self.storage)
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    size = self.get_size()

    # Base case:
    # This check avoids an edge case where the test tries to delete 0 from [0]
    if(size == 0):
      #print('no storage left, bailing. storage:', self.storage)
      return

    parent = self.storage[index]
    #print('\n')
    #print('in sift_down, index:', index)
    #print('in sift_down, parent at index', index, 'is', parent)
    left_index = Heap.get_left_child_index(index)
    right_index = Heap.get_right_child_index(index)
    #print('in sift_down, left child index is:', left_index)
    #print('in sift_down, right child index is:', right_index)
    #print('storage length:', len(self.storage))
    #print('storage size tho:', self.get_size())
    #print('about to look up left and right, storage:', self.storage)

    # test to make sure left index isn't out of range:
    if left_index <= size:
      left = self.storage[left_index]
    else:
      left = float('-inf')

    # test to make sure right index isn't out of range:
    if right_index <= size:
      right = self.storage[right_index]
    else:
      right = float('-inf')

    #print('LEFT:', left)
    #print('RIGHT:', right)
    #print('STORAGE:', self.storage)
    #print('in sift_down, left child:', left)
    #print('in sift_down, right child:', right)

    # Base case: If both children are -infinity, the node has no
    # children and we need to bail out:
    if math.isinf(left) and math.isinf(right):
      #print('node has no children and has found its proper place')
      #print('final storage:', self.storage)
      return

    child = left if left > right else right
    child_index = self.storage.index(child)

    if parent < child:
      #print('parent is less than child:', parent, '<', child)
      #print('swapping parent & child')
      self.storage[child_index], self.storage[index] = parent, child
      #print('new storage:', self.storage)
      #print('calling sift_down again with new index:', child_index)
      self._sift_down(child_index)

    else:
      #print('node has sifted down and found its proper place')
      #print('final storage:', self.storage)
      return

# My own tests:
#test_heap = Heap()
#test_heap.insert(100)
#print('\n')
#test_heap.insert(19)
#print('\n')
#test_heap.insert(21)
#print('\n')
#test_heap.insert(47)
#print('\n')
#test_heap.insert(35)
#print('\n')
#test_heap.insert(29)
#print('\n')
#test_heap.insert(101)
# Testing delete:
#test_heap.delete()
#test_heap.delete()
# Testing get_max after deleting:
#test_heap.get_max()

