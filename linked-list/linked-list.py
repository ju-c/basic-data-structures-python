class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iterative_linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def recursive_linked_list_values(head):
    values = []
    _recursive_linked_list_values(head, values)
    return values


def _recursive_linked_list_values(head, values):
    if head is None:
        return
    values.append(head.val)
    _recursive_linked_list_values(head.next, values)


def iterative_get_node_value(head, index):
    current = head
    count = 0

    while current is not None:
        if count is not index:
            current = current.next
            count += 1
        else:
            return current.val

    return None


def recursive_get_node_value(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val

    return recursive_get_node_value(head.next, index - 1)


def iterative_sum_linked_list(head):
    total_sum = 0
    current = head

    while current is not None:
        total_sum += current.val
        current = current.next

    return total_sum


def recursive_sum_linked_list(head):
    if head is None:
        return 0

    return head.val + recursive_sum_linked_list(head.next)


def iterative_reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def recursive_reverse_linked_list(head, prev=None):
    if head is None:
        return prev

    next = head.next
    head.next = prev

    return recursive_reverse_linked_list(next, head)


a = Node(2)
b = Node(5)
c = Node(-1)
d = Node(3)
e = Node(8)

a.next = b
b.next = c
c.next = d
d.next = e

print(iterative_linked_list_values(a))
print(recursive_linked_list_values(a))

print(iterative_sum_linked_list(a))
print(recursive_sum_linked_list(a))

print(iterative_get_node_value(a, 4))
print(recursive_get_node_value(a, 4))

iterative_reverse_linked_list(a)
print(iterative_linked_list_values(e))

recursive_reverse_linked_list(e)
print(recursive_linked_list_values(a))
