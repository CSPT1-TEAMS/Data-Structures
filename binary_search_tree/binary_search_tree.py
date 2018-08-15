class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = BinarySearchTree(value)
    elif value > self.value:
      if self.right == None: 
        self.right = BinarySearchTree(value)
        return
      else:
        self.right.insert(value)
    else: #value <= self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
        

  def contains(self, target):
    if self.value == None:
      return False
    if self.value == target:
      return True
    if target > self.value and self.right != None:
      return self.right.contains(target)
    if target <= self.value and self.left != None:
      return self.left.contains(target)
    return False


  def get_max(self):
    if self.value == None:
      return None
    if self.right == None:
      return self.value
    else: #self.right != None:
      return self.right.get_max()
    
