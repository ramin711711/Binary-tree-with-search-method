class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def add(self, data):
        if self.data == None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data and self.left:
            return self.left.search(value)
        elif value > self.data and self.right:
            return self.right.search(value)
        return False

    def tree(self):
        if self.left:
            self.left.tree()
        print(self.data)
        if self.right:
            self.right.tree()
            
root = Node('g')
root.add('b')
root.add('m')
root.add('n')
root.add('p')
root.add('v')
root.add('d')
root.add('a')
root.tree()

a = input('Which number are you looking for? ')
if root.search(a):
    print(f"Binary has '{a}'")
else:
    print(f"Binary tree doesn't have '{a}'")