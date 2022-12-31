
#value - anything from strings integers etc
# Node - Next node

class linkedListNode:
    def __init__(self, value, nextNode =None):
        self.value = value
        self.nextNode = nextNode


node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1

while True:
    print(currentNode.value , "->" , end ="")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode