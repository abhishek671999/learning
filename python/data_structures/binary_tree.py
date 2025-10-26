from turtle import left


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.length = 0
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root:
            current_node = self.root
            while True:
                if current_node.value < new_node.value:
                    if not current_node.right:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right
                else:
                    if not current_node.left:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
        else:
            self.root = new_node
    
    def delete(self, value):
        pass
            
    
    def lookup(self, value):
        if not self.root:
            return False
        else:
            current_node = self.root
            while current_node:
                if value == current_node.value:
                    return True
                elif value > current_node.value:
                    current_node = current_node.right
                elif value < current_node.value:
                    current_node = current_node.left
            return False
    
def traverse(node):
    if node is None:
        return None
    tree = {'value': node.value}
    tree['left'] = traverse(node.left)
    tree['right'] = traverse(node.right)
    return tree

if __name__ == '__main__':
    binary_tree = BinaryTree()  
    binary_tree.insert(10)
    binary_tree.insert(20)
    binary_tree.insert(5)
    binary_tree.insert(16)
    print(traverse(binary_tree.root))
    print(binary_tree.lookup(16))
    