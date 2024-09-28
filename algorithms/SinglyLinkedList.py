class Node:
  def __init__(self, data = None, next = None) -> None:
    self.data = data
    self.next = next

  def setData(self, data):
    self.data = data

  def getData(self):
    return self.data
  
  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next
  
  def hasNext(self):
    return self.next != None
  
class LinkedList(object):
  def __init__(self, node = None) -> None:
    self.length = 0
    self.head = node

  def getLength(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.next
    return count
  
  def insertAtBeginning(self, data):
    newNode = Node()
    newNode.data = data
    if self.length == 0:
      self.head = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1

  def insertAtEnding(self, data):
    newNode = Node()
    newNode.data = data
    current = self.head
    while current.next != None:
      current = current.next
    current.next = newNode
    self.length += 1

  def insertBetween(self, pos, data):
    if pos > self.length or pos < 0:
      return None
    if pos == 0:
      self.insertAtBeginning(data)
    else:
      if pos == self.length:
        self.insertAtEnding(data)
      else:
        newNode = Node()
        newNode.setData(data)
        current = self.head
        count = 1
        while count < pos - 1:
          current = current.next
          count += 1
        newNode.setNext(current.next)
        current.next = newNode
        self.length += 1
    
  #Deleting from LL
  def deleteFirstNode(self):
    if self.length == 0:
      print("List is empty")
    else:
      self.head = self.head.next
      self.length -= 1

  def deleteLastNode(self):
    if self.length == 0:
      print("List is empty")
    if self.length == 1:
      self.head = None
      self.length = 0
    else:
      current = self.head
      previous = self.head
      while current.next != None:
        previous = current
        current = current.next
      previous.next = None
      self.length -= 1

  # Delete with Node
  def deleteByNode(self, node ):
    if self.length == 0:
      raise ValueError("List is empty")
    else:
      current = self.head
      previous = None
      found = False
      while not found:
        if current == node:
          found = True
        elif current == None:
          raise ValueError("Node not in list?")
        else:
          previous = current
          current = current.next
    if previous is None:
      self.head = current.next
    else:
      previous = current.next
    self.length -= 1

# Delete by value
  def deleteByValue(self, value):
    if self.length == 0:
      raise ValueError("List is empty")
    else:
      current = self.head
      previous = None
      found = False
      while not found:
        if current.data == value:
          found = True
        elif current == None:
          raise ValueError("Node not in list?")
        else:
          previous = current
          current = current.next
    if previous == None:
      self.head = current.next
    else:
      previous = current.next
    self.length -= 1

# Delete by position
  def deleteByPosition(self, position):
    if self.length == 0:
      raise ValueError("List is empty")
    elif position == 1:
      self.head = None
    else:
      current = self.head
      previous = None
      count = 1
      while count <= position:
        count += 1
        previous = current
        current = current.next
      previous.next = current.next
      self.length -= 1
      

# Driver Code
ll = LinkedList()

def printLinkedList(ll):
  current = ll.head
  while current is not None:
    print(current.getData(), end=" -> ")
    current = current.getNext()
  print("None")

# Insert elements at the beginning
ll.insertAtBeginning(10)
ll.insertAtBeginning(20)
ll.insertAtBeginning(30)

print("LinkedList after inserting at the beginning:")
printLinkedList(ll)

# Insert elements at the end
ll.insertAtEnding(40)
ll.insertAtEnding(50)

print("LinkedList after inserting at the end:")
printLinkedList(ll)

# Insert element at position 2
ll.insertBetween(2, 25)

print("LinkedList after inserting at position 2:")
printLinkedList(ll)

# Delete the first node
ll.deleteFirstNode()

print("LinkedList after deleting the first node:")
printLinkedList(ll)

# Delete the last node
ll.deleteLastNode()

print("LinkedList after deleting the last node:")
printLinkedList(ll)

# Delete an intermediate node
# Assuming we're deleting the node with data '25'
# To find the node with data '25'
# current = ll.head
# while current is not None and current.getData() != 25:
#     current = current.getNext()

# if current is not None:
#     ll.deleteByNode(current)
#     print("LinkedList after deleting the node with data 25:")
#     printLinkedList(ll)
# else:
#     print("Node with data 25 not found.")


