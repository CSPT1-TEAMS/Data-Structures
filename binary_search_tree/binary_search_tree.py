class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
      
  def contains(self, target):
    if target == self.value:
      return True
    if target < self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    if target >= self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    return False

  def get_max(self):
    if self.right is None:
      return self.value
    return self.right.get_max()

  def get_min(self):
    if self.left is None:
      return self.value
    return self.left.get_max()
