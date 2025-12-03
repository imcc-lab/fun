class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} into the queue.")
    def dequeue(self):
        if not self.queue:
            print("Queue Underflow! Cannot dequeue from empty queue.")
            return
        removed = self.queue.pop(0)
        print(f"Dequeued element: {removed}")
    def peek(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print(f"Front element: {self.queue[0]}")
    def reverse(self):
        if not self.queue:
            print("Queue is empty. Cannot reverse.")
            return

        stack = []  # temporary stack
        # Move all elements from queue to stack
        while self.queue:
            stack.append(self.queue.pop(0))
        # Move elements back from stack to queue
        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed successfully.")

        # Utility method: display queue

    def display(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Current Queue (front → rear): ", end="")
        for item in self.queue:
            print(item, end=" ")
        print("\n")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(59)
q.enqueue(90)
q.enqueue(23)
q.display()

q.peek()

q.dequeue()
q.display()

q.reverse()
print("Reversed : ")
q.display()
