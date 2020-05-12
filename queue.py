import time
start = time.time()

class Queue:

    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if(len(self.queue) < 1):
            return None
        return self.queue.pop(0)
    
    def display(self):
    
        print(self.queue)

    def size(self):
        return len(self.queue)
    def min(self):
        print(min(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print("Current Queue element")
q.display()

q.dequeue()

print("After removing an element")
q.display()
print("Find the min item in this queue")
q.min()
end = time.time()
print("Time(sec) taken our program =",(end-start)*1000,end="")
print("\nThe complexity of my program is O(n)")
