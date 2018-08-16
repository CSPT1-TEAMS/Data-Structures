class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value == None:
      self.value = BinarySearchTree(value)
    elif value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
        return
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    #checks if tree exists

    if self.value == None:
      return False

    # recursion base case

    if self.value == target:
      return True

    # if the value exists, or doesnt exist

    if target < self.value:
      if not self.left == None:
        return self.left.contains(target)
    if target > self.value:
      if not self.right == None:
        return self.right.contains(target)

    #second base case
    return False

  def get_max(self):
    if self.value == None:
      return None
    
    if self.right == None:
      return self.value
    return self.right.get_max()