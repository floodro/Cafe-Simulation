class Node:
    value = 0;
    next_node = None
    timeStamp = 0
    time = 0
    LineNo = 0

    def __init__ (self, data, time, no):
        self.value = data;
        self.timeStamp = time; 
        self.LineNo = no;
        next_node = None

    def getVal(self):
        return self.value;

    def setNext(self, num):
        self.next_node = num;

    def getNext(self):
        return self.next_node;
        
    def getLineNo(self):
        return self.LineNo;

    def getTime(self):
        return self.time;

class LinkedList:
    head = ""
    tail = ""
    length = 0
    
    def append(self, names, time, x):
        newNode = Node(names, time, x);
        if (self.length == 0):
            self.head = newNode;
            self.tail = newNode;

        else:
            self.tail.setNext(newNode);
            self.tail = newNode;
        self.length += 1; 

    def remove(self,pos):
        if pos == 0:
            previous = self.head;
            self.head = self.head.getNext();
            previous.setNext(None);
        self.length -= 1
    
    def nodeAt(self, pos):
        current = self.head;
        i = 0

        while i < pos:
            current = current.getNext();
            i += 1;
        return current;

    def getLength(self):
        return str(self.length);
    
    def print(self):
        current = self.head
        if current == "":
            print("There is no customer yet.")
        else:
            while current != None:
                print(current.getVal(), " ", end = "");
                current = current.getNext();
            
