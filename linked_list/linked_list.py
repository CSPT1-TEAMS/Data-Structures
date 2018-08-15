"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value #header
    self.next_node = next_node #pointer

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if self.head == None:
      return None
    elif self.head.next_node == None:
      prev_value = self.head.value
      self.tail = None
      self.head = None
      return prev_value

    else:
      prev_value = self.head.value
      self.head = self.head.next_node


      return prev_value

  def contains(self, value):
    cur_node = self.head
    while cur_node:
      if cur_node.value == value:
        return True
      else:
        cur_node = cur_node.next_node
    return False

  def get_max(self):
    if self.head == None:
      return None

    current = self.head
    big_num = current.value
      
    while not current == None:
      if current.value > big_num:
        big_num = current.value

      current = current.next_node

    return big_num