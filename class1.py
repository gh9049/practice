
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Linkedlist:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.lenght = 1
    
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.lenght == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.lenght+=1


my_linked_list = Linkedlist(1)

my_linked_list.append(2)

my_linked_list.print_list()