class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    # add to array
    self.storage.append( value )
    # bubble _bubble_up
    self._bubble_up( self.size + 1 )
    # # update size
    self.size += 1

  def delete(self):
    # save value
    # swap first and last elements
    # delete array
    # sift down
    # update dize
    # return value
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size = self.size - 1
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]
    # should be one line...where can we A:WAYS
    # find the biggest value
  def get_size(self):
    # return self.size
    pass

  def _bubble_up(self, index):
    # if node smaller than parent
    # while index // 2 > 0:
    #   if self.storage[index] < self.storage[ index // 2 ]:
    #   # while node > its arent
    #     #swap
    #     # swap parent a& valie @ index
    #     # recursive call
    #     tmp = self.storage[index // 2]
    #     self.storage[index//2] = self.storage[index]
    #     self.storage[index] = tmp
    # index = index // 2
    if self.storage[index] < self.storage[ (index // 2) ]:
      return
    else:
      old_parent = self.storage[(index // 2)]
      new_parent = self.storage[index]
      self.storage[ (index // 2) ] = new_parent
      self.storage[index] = old_parent
    return

  def _sift_down(self, index):
    # insert last element at (empty) root
    # while index < its children
      #swap
    pass
