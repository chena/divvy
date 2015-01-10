class Node(object):
    def __init__(self, value, left=None, right=None, parent=None, num=0):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        self.num = num

def sum_paths(node, target_sum, paths=[], lst=[]):
    """
    print out all paths that sum up to a given value in a binary tree
    assume all positive numbers
    assume nodes have reference to their parents 
    """
    lst.append(node.value)
    so_far = sum(lst)
    if so_far == target_sum:
        paths.append(lst)
    if so_far < target_sum:
        if node.left:
            sum_paths(node.left, target_sum, paths, lst[:])
            sum_paths(node.left, target_sum, paths, [])
        if node.right:
            sum_paths(node.right, target_sum, paths, lst[:])
            sum_paths(node.right, target_sum, paths, [])
    return paths

def preorder(root, nodes=[]):
    nodes.append(root.value)
    if root.left:
        preorder(root.left, nodes)
    if root.right:
        preorder(root.right, nodes)
    return nodes

def levelorder(node):
    levels = []
    q = []
    q.append(node)
    # we need to keep track of number of nodes at the current level and next level
    # to know when to print a new line
    curr, next = 1, 0
    level = []
    while q:
        node = q.pop(0)
        level.append(node.value)
        curr -= 1
        if node.left:
            q.append(node.left)
            next += 1
        if node.right:
            q.append(node.right)
            next += 1
        if not curr:
            levels.append(level)
            level = []
            curr = next
            next = 0
    return levels

def tree_depth(node):
    if not node:
        return 0
    return 1 + max([tree_depth(node.left), tree_depth(node.right)])

def check_balance(node):
    return max([tree_depth(node.left), tree_depth(node.right)]) - min ([tree_depth(node.left), tree_depth(node.right)]) <= 1

def inorder(node, lst=[]):
    if not node:
        return
    if node.left:
        inorder(node.left)
    lst.append(node.value)
    if node.right:
        inorder(node.right)
    return lst


def to_tree(nodes, start, end):
    """
    convert an array of nodes into a tree with minimum height
    """
    if start > end:
        return
    mid = (start + end) / 2
    n = Node(nodes[mid])
    n.left = to_tree(nodes, start, mid - 1)
    n.right = to_tree(nodes, mid + 1, end)
    return n

def sum_tree(node):
    if not node:
        return 0
    return node.value + sum_tree(node.left) + sum_tree(node.right)

"""
n4 = Node(4)
n3 = Node(3)
n6 = Node(6)
n7 = Node(7)

n2 = Node(2, n4, n3)
n5 = Node(5, n6, n7)
n1 = Node(1, n2, n5)
inorder(n1)
"""

def bst_second_largest(node):
    """
    hint: largest = rightmost child
    """
    pre = None
    while node.right:
        pre = node
        node = node.right
    return pre
