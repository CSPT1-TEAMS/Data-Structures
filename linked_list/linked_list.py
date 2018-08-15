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
    new_node = Node(value)
    if self.head == None:
      # set head & tail equal to the same node obj
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
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
    # if head DNE, return None
    # else . set head.next = head, return head.value
  def contains(self, value):
    curr_node = self.head
    while curr_node:
      if curr_node.get_value() == value:
        return True
      else:
        curr_node = curr_node.get_next()

  def get_max(self):
    if self.head is None:
      return None
    val = self.head.get_value()
    curr_node = self.head.get_next()
    while curr_node:
      if curr_node.get_value() > val:
        val = curr_node.get_value()
      else:
        curr_node = curr_node.get_next()
    return val
    