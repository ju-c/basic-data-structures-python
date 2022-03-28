class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, value):
    if root.data:
        if value < root.data:
            if root.left is None:
                root.left = Node(value)
            else:
                insert_node(root.left, value)
        elif value > root.data:
            if root.right is None:
                root.right = Node(value)
            else:
                insert_node(root.right, value)
    else:
        root.data = value


def delete_node(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete_node(root.left, value)
        return root
    if value > root.data:
        root.right = delete_node(root.right, value)
        return root
    if root.right is None:
        return root.left
    if root.left is None:
        return root.right

    min_larger_node = root.right

    while min_larger_node.left:
        min_larger_node = min_larger_node.left

    root.data = min_larger_node.data
    root.right = delete_node(min_larger_node.data)

    return root


def show_tree(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return print(result)


def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root.data)
    if root.right:
        print_tree(root.right)


def exists_in_tree(root, key):
    if key == root.data:
        return True
    if key < root.data:
        if root.left is None:
            return False
        return exists_in_tree(root.left, key)
    elif key > root.data:
        if root.right is None:
            return False
        return exists_in_tree(root.right, key)


def get_min(root):

    current = root

    while current.left is not None:
        current = current.left

    return current.data


def get_max(root):

    current = root

    while current.right is not None:
        current = current.right

    return current.data


def get_height(root):
    return 1 + max(
        get_height(root.left) if root.left else -1,
        get_height(root.right) if root.right else -1
    )


def is_balanced(root):
    def _balanced(root):
        if root is None:
            return (True, 0)
        leftBalanced, leftHeight = _balanced(root.left)
        rightBalanced, rightHeight = _balanced(root.right)
        if leftBalanced and rightBalanced and abs(leftHeight - rightHeight) < 2:
            currentHeight = max(leftHeight, rightHeight) + 1
            return (True, currentHeight)
        return (False, None)
    return _balanced(root)[0]


def reverse_binary_tree(root):
    if root is None:
        return root

    root.left, root.right = root.right, root.left

    reverse_binary_tree(root.left)
    reverse_binary_tree(root.right)

    return root


tree = Node(20)
insertion = [1, 2, 8, 9, 11, 12, 18, 19]
for i in insertion:
    insert_node(tree, i)
print_tree(tree)
delete_node(tree, 11)
print_tree(tree)
print(is_balanced(tree))
