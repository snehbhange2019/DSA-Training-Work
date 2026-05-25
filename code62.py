def delete(self):
    if self.isEmpty():
        print("Queue is empty")
    else:
        ele = self.queue[self.front]
        for i in range(1, self.rear + 1):
            self.queue[i - 1] = self.queue[i]

        self.queue.pop() 
        self.rear -= 1
        print(ele, "is deleted")