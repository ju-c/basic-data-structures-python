class Queue:

    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if len(self.queue) < 1:
            return None
        self.queue.pop(0)

    def __str__(self):
        return str(self.queue)


q = Queue()

q.add('1')
q.add('2')
q.add('3')
q.add('4')
q.add('5')

print(q)
q.remove()
print(q)
q.remove()
print(q)
q.remove()
print(q)
q.remove()
print(q)
q.remove()
print(q)
