class Queue:
    def __init__(self):
        self.queue = []
    
    # Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    # Remove an element from the front of the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        item = self.queue.pop(0)
        print(f"Dequeued: {item}")
        return item
    
    # Display the current queue
    def display(self):
        print(f"Queue: {self.queue}")
    
    # Return the size of the queue
    def size(self):
        return len(self.queue)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()

print(f"Queue size: {q.size()}")
