"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

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
    new_node = Node( value )
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node


  def remove_head(self):
    if self.head == None:
      return None
    elif self.head.get_next() is None:
      node = self.head
      self.head = None
      self.tail = None
    else:
      node = self.head
      self.head = node.get_next()
    return node.get_value()

  def contains(self, value):
    cur_node = self.head
    while cur_node:
      if cur_node.get_value() == value:
        return True
      else:
        cur_node = cur_node.get_next()
    

  def get_max(self):
    if self.head == None:
      return None
    val = self.head.get_value()
    cur_node = self.head.get_next()
    while cur_node:
      if cur_node.get_value() > val:
        val = cur_node.get_value()
      else:
        cur_node = cur_node.get_next()
    return val
