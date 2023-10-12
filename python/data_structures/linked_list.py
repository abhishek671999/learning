class Node:
    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next_pointer = next_pointer


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next_pointer is not None:
                node = node.next_pointer
            else:
                node.next_pointer = new_node

    def update(self, index, value):
        if index == 0:
            self.head.value = value
        else:
            counter = 0
            node = self.head
            while counter < index:
                if node.next_pointer is None:
                    node.next_pointer = Node(value)
                    break
                else:
                    node = node.next_pointer
                    counter += 1
            else:
                node.value = value

    def delete_by_index(self, index):
        counter = 0
        node = self.head
        if index == 0:
            self.head = self.head.next_pointer
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
        node = self.head
        while node.next_pointer is not None:
            if node.next_pointer.value == value:
                node.next_pointer = node.next_pointer.next_pointer
            else:
                node = node.next_pointer

    def display(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next_pointer
        else:
            print()

    def delete_all_duplicates(self):
        new_list = LinkedList()
        current_node = self.head
        next_node = self.head
        flag = True
        print('Removing duplicates')
        while next_node is not None:
            next_node = next_node.next_pointer
            if next_node is not None and next_node.value == current_node.value:
                flag = False
                while next_node.value != current_node.value:
                    next_node = next_node.next_pointer
            else:
                if flag:
                    new_list.append(current_node.value)
                current_node = next_node
                flag = True
        else:
            self.head = new_list.head


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(5)
    # linked_list.append(6)
    linked_list.display()
    linked_list.delete_all_duplicates()
    linked_list.display()
    # linked_list.delete_by_index(5)
    # linked_list.delete_by_value(4)
    # linked_list.update(10, 5)

