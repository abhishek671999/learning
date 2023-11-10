class Node:
    def __init__(self, value, next_pointer=None, prev_pointer=None):
        self.value = value
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        node = self.head
        if self.head is None:
            self.head = new_node
        else:
            while node.next_pointer is not None:
                node = node.next_pointer
            else:
                new_node.prev_pointer = node
                node.next_pointer = new_node

    def update(self, index, value):
        counter = 0
        node = self.head
        while counter < index:
            counter += 1
            node = node.next_pointer
        else:
            node.value = value

    def delete_by_index(self, index):
        if index == 0:
            self.head = self.head.next_pointer
            self.head.prev_pointer = None
        else:
            counter = 0
            node = self.head
            while counter < index-1:
                counter += 1
                if node.next_pointer is None:
                    break
                else:
                    node = node.next_pointer
            else:
                node.next_pointer = node.next_pointer.next_pointer

    def delete_by_value(self, value):
        if value == self.head.value:
            self.head = self.head.next_pointer
            self.head.prev_pointer = None
        else:
            node = self.head
            while node.next_pointer is not None:
                print(node.next_pointer.value, value, end='')
                if node.next_pointer.value == value:
                    print('value true')
                    node.next_pointer.next_pointer = node
                    node.next_pointer = node.next_pointer.next_pointer
                else:
                    node = node.next_pointer
                print()

    def display(self):
        node = self.head
        while node is not None:
            print(node.value, end=' ')
            node = node.next_pointer
        else:
            print()


if __name__ == '__main__':
    reversed_linked_list = ReversedLinkedList()
    reversed_linked_list.append(1)
    reversed_linked_list.append(2)
    reversed_linked_list.append(2)
    reversed_linked_list.append(3)
    reversed_linked_list.append(3)
    reversed_linked_list.append(4)
    reversed_linked_list.append(5)
    reversed_linked_list.append(6)
    reversed_linked_list.display()
    reversed_linked_list.update(1, 3)
    reversed_linked_list.display()
    reversed_linked_list.delete_by_value(3)
