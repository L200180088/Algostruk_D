##nomer1
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

def cetakHexa(data):
    a = Stack()
    hx = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        a.push(hx[sisa])
    st=""
    for i in range(len(a)):
        st = st + str(a.pop())
    return st

##nomer2
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

nilai = Stack()         #membuat sebuah objek dari kelas Stack yang disimpan di variabel "nilai"
for i in range(16):     #untuk i dalam range 16
    if i % 3 == 0:      #jika i habis dibagi 3, maka:
        nilai.push(i)   #meletakkan i di variabel "nilai"

print(nilai.items)


##nomer3
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

nilai1 = Stack()        #membuat sebuah objek dari kelas Stack yang disimpan di variabel "nilai1"
for i in range (16) :   #untuk i dalam range 16
    if i % 3 == 0:      #jika i habis dibagi 3, maka:
        nilai1.push(i)  #meletakkan i di variabel "nilai1"
    elif i % 4 == 0:    #dan jika i habis dibagi 4, maka:
        nilai1.pop()    #mengembalikan nilai dari item posisi paling atas dari variabel
                        #"nilai" lalu menghapusnya "nilai"

print(nilai1.items)

##nomer4
class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    def getFrontMost(self): #untuk mengetahui item yang paling depan tanpa menghapusnya
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[0]
    def getRearMost(self):  #untuk mengetahui item yang paling belakang tanpa menghapusnya
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[-1]

c = Queue()
c.enqueue(28)
c.enqueue(19)
c.enqueue(45)
c.enqueue(13)
c.enqueue(7)

print (c.qlist)
print (c.getFrontMost())
print (c.getRearMost())
print (c.qlist)

##nomer5
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority) #memanggil object _PriorityQEntry
        self.qlist.append(entry)
    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item


class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

d = PriorityQueue()
d.enqueue("Jeruk", 4)
d.enqueue("Tomat", 2)
d.enqueue("Mangga", 0)
d.enqueue("Duku", 5)
d.enqueue("Pepaya", 2)

print (d.dequeue())
print (d.dequeue())
print (d.dequeue())
print (d.dequeue())
print (d.dequeue())

