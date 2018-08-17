class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
      if self.left is not None:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
        return
    elif self.value < value:
      if self.right is not None:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
        return
    return

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value:
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False
    elif target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False

  def get_max(self):
    while self.right:
      self = self.right
    return self.value
