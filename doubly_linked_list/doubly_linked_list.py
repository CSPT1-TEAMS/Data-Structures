class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = value
    
  def insert_before(self, value):
    new_node = value
    self.tail.next = new_node

  def delete(self):
    pass

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    # create new_node
    new_node = ListNode( value )
    #if head DNE, head & tail = new_node
    #add to head or remove from the tail
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.prev = self.tail
      self.tail = new_node

    return

    # else
      # head.prev = new_node
      # update head.. head = new_node
      # update head... head = new_node
    pass

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
