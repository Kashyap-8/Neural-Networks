
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        node.append("None")
        return " --> ".join(nodes)



llist = LinkedList()

print(llist)
first_node = Node('a')
llist.head = first_node
print(llist)