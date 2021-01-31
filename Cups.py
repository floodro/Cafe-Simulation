class Node:
    value = ""
    next_node = 0

    def __init__(self, data):
        self.value = data;

    def getVal(self):
        return self.value;

    def setNext(self, nxt):
        self.next_node = nxt;
        
    def getNext(self):
        return self.next_node;

class Stack:
    size = 0;
    head = ""
    tail = ""

    def push(self, data):
        newNode = Node(data)
        current = self.head;
        
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1

    def pop(self):
        temp = self.tail;
        if self.size == 0:
            print("Your stack is empty.")
        else:
            current = self.head;
            i = 0
            
            if self.size > 0: 
                while i < self.size - 2: 
                    current = current.getNext(); 
                    i += 1;
                    
            self.tail = current
            current.setNext(None)
            del(temp) 
            self.size = self.size - 1; 
    
    def Print(self):
        current = self.head;
        i = 0;
        print("Your current stack is ", end=' ');
        while i < self.size:
            print(current.getVal(),end=' ');
            current = current.getNext();
            i += 1;
    
