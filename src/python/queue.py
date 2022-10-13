class queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        value = self.queue[0]
        self.queue.pop(0)
        return value

    def get_rear(self):
        return self.queue[-1]

    def get_front(self):
        return self.queue[0]
