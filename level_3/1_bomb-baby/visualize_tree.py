class Node:
    def __init__(self, m, f, left=None, right=None):
        self.mach = m
        self.facula = f
        self.left = left
        self.right = right

    def __str__(self):
        return '({},{})'.format(self.mach, self.facula)

    def generate_left(self):
        self.left = Node(self.mach + self.facula, self.facula)

    def generate_right(self):
        self.right = Node(self.mach, self.facula + self.mach)

    def generate_children(self):
        self.generate_left()
        self.generate_right()


def print_tree(root):
    h = height(root)
    for i in range(1, h + 1):
        print_depth_level(root, i)


def print_depth_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root)
    elif level > 1:
        print_depth_level(root.left, level - 1)
        print_depth_level(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        return max(lheight, rheight) + 1


def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        given_spiral_level(root, i)

def given_spiral_level(root, level):
    if root is None:
        return root

    if level == 1:
        print()


root = Node(1, 1)
root.generate_children()
print(root)
print_tree(root)
