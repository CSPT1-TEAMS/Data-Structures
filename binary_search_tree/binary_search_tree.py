class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree( value )
    if value < self.value:
      if self.left is None:
        self.left = node
      else:
        self.left.insert(value)
      return
    if self.right is None:
      self.right = node
    else:
      self.right.insert(value)
    return
    
  def contains(self, target):
    if self.value == target:
      return True
    if target <= self.value:
      if not self.left:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if not self.right:
        return False
      return self.right.contains(target)

  def get_max(self):
    if not self.right:
      return self.value
    return self.right.get_max()

